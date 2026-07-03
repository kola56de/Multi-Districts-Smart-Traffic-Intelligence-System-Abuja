import streamlit as st
import pandas as pd
import pydeck as pdk
import networkx as nx
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

st.set_page_config(layout="wide")
st.title("🚦 Smart Traffic Intelligence System (Abuja)")

# ----------------------------
# DATA (MAITAMA + WUSE)
# ----------------------------
data = {
    "start": [
        "Banex Junction","Banex Junction","Banex Junction",
        "Hospital Junction","Hospital Junction",
        "Wuse Market Junction","Wuse Market Junction",
        "Berger Junction","Berger Junction","Berger Junction",
        "Garki Market","Garki Market","Eagle Square"
    ],
    "end": [
        "Hospital Junction","University Junction","Wuse Market Junction",
        "University Junction","Wuse Market Junction",
        "Head of Service","University Junction",
        "Garki Market","Eagle Square","Area 10",
        "Eagle Square","Area 10","Area 10"
    ],
    "length_km": [2.5,3.9,1.7,1.3,2.5,3.6,1.0, 8.3,5.6,6.9,5.5,3.8,8.2],
    "time_sec": [471,364,101,132,227,185,149, 466,348,2046,843,665,358],
    "avg_speed": [19,29,62,35,39,37,25, 33,31,12,23,21,41],
    "district": [
        "Maitama","Maitama","Maitama","Maitama","Maitama","Maitama","Maitama",
        "Wuse","Wuse","Wuse","Wuse","Wuse","Wuse"
    ],
    "start_lat": [9.084,9.084,9.084,9.08,9.08,9.07,9.07, 9.06,9.06,9.06,9.05,9.05,9.07],
    "start_lon": [7.489,7.489,7.489,7.5,7.5,7.495,7.495, 7.45,7.45,7.45,7.48,7.48,7.49],
    "end_lat": [9.08,9.072,9.085,9.072,9.085,9.06,9.06, 9.05,9.07,9.04,9.07,9.04,9.04],
    "end_lon": [7.5,7.51,7.48,7.51,7.48,7.47,7.47, 7.48,7.49,7.46,7.49,7.46,7.46],
}

df = pd.DataFrame(data)

# ----------------------------
# TIME OF DAY SIMULATION
# ----------------------------
time_of_day = st.selectbox("🕒 Time of Day", ["Off-Peak", "Normal", "Rush Hour"])

def adjust_time(row):
    if time_of_day == "Rush Hour":
        return row["time_sec"] * 1.5
    elif time_of_day == "Off-Peak":
        return row["time_sec"] * 0.8
    return row["time_sec"]

df["adjusted_time"] = df.apply(adjust_time, axis=1)
df["adjusted_speed"] = df["length_km"] / (df["adjusted_time"]/3600)

# ----------------------------
# TRAFFIC COLORS
# ----------------------------
def get_color(speed):
    if speed >= 50:
        return [0,255,0]
    elif speed >= 30:
        return [255,165,0]
    else:
        return [255,0,0]

df["color"] = df["adjusted_speed"].apply(get_color)

# ----------------------------
# FILTERS
# ----------------------------
st.sidebar.header("🔍 Filters")

district_filter = st.sidebar.multiselect(
    "District",
    df["district"].unique(),
    default=df["district"].unique()
)

def traffic_label(speed):
    if speed >= 50:
        return "Light"
    elif speed >= 30:
        return "Moderate"
    else:
        return "Heavy"

df["traffic"] = df["adjusted_speed"].apply(traffic_label)

traffic_filter = st.sidebar.multiselect(
    "Traffic Level",
    ["Light","Moderate","Heavy"],
    default=["Light","Moderate","Heavy"]
)

df = df[df["district"].isin(district_filter)]
df = df[df["traffic"].isin(traffic_filter)]

# ----------------------------
# MIDPOINTS FOR ETA
# ----------------------------
df["mid_lat"] = (df["start_lat"] + df["end_lat"]) / 2
df["mid_lon"] = (df["start_lon"] + df["end_lon"]) / 2
df["label"] = df["adjusted_time"].astype(int).astype(str) + " sec"

# ----------------------------
# MODEL
# ----------------------------
if len(df) > 2:
    X = df[["length_km", "adjusted_time"]]
    y = df["adjusted_speed"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestRegressor(n_estimators=200)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    st.subheader("🤖 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📈 R² Score", f"{r2:.2f}")

with col2:
    st.metric("📉 MAE", f"{mae:.2f}")

with col3:
    st.metric("🤖 Model", "Random Forest")

# ----------------------------
# ROUTE OPTIMIZATION
# ----------------------------
st.subheader("🔄 Route Optimization")

locations = sorted(set(df['start']).union(set(df['end'])))
start_node = st.selectbox("Start Location", locations)
end_node = st.selectbox("Destination", locations)

G = nx.Graph()
for _, row in df.iterrows():
    G.add_edge(row['start'], row['end'], weight=row['adjusted_time'])

path = None

if st.button("Find Best Route"):
    try:
        path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')
        cost = nx.shortest_path_length(G, source=start_node, target=end_node, weight='weight')

        st.success(" → ".join(path))
        st.info(f"ETA: {int(cost)} sec")
    except:
        st.error("No route found")

# ----------------------------
# MAP VISUALIZATION (NO MAPBOX)
# ----------------------------
st.subheader("🗺️ Traffic Map")

view_state = pdk.ViewState(
    latitude=df["start_lat"].mean(),
    longitude=df["start_lon"].mean(),
    zoom=12,
    pitch=45,
)

line_layer = pdk.Layer(
    "LineLayer",
    data=df,
    get_source_position='[start_lon, start_lat]',
    get_target_position='[end_lon, end_lat]',
    get_color="color",
    get_width=6,
)

text_layer = pdk.Layer(
    "TextLayer",
    data=df,
    get_position='[mid_lon, mid_lat]',
    get_text="label",
    get_size=14,
    get_color=[0,0,0],
)

layers = [line_layer, text_layer]

# Highlight best route
if path:
    coords = {}
    for _, row in df.iterrows():
        coords[row['start']] = (row['start_lat'], row['start_lon'])
        coords[row['end']] = (row['end_lat'], row['end_lon'])

    route_data = []
    for i in range(len(path)-1):
        s = coords[path[i]]
        e = coords[path[i+1]]

        route_data.append({
            "start_lon": s[1],
            "start_lat": s[0],
            "end_lon": e[1],
            "end_lat": e[0],
        })

    route_df = pd.DataFrame(route_data)

    route_layer = pdk.Layer(
        "LineLayer",
        data=route_df,
        get_source_position='[start_lon, start_lat]',
        get_target_position='[end_lon, end_lat]',
        get_color=[255,0,0],
        get_width=10,
    )

    layers.append(route_layer)

deck = pdk.Deck(
    layers=layers,
    initial_view_state=view_state,
    map_provider="carto",   # 🔥 NO MAPBOX NEEDED
    map_style="light"
)

st.pydeck_chart(deck)

# ----------------------------
# LEGEND
# ----------------------------
st.markdown("""
### 🧭 Traffic Legend
- 🟢 Light Traffic  
- 🟡 Moderate Traffic  
- 🔴 Heavy Traffic  
""")
