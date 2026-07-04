# 🚦 Multi-District Smart Traffic Intelligence System (Abuja)

An AI-powered traffic intelligence platform built with **Python, Streamlit, Machine Learning, GIS Mapping, and Route Optimization Algorithms** to analyze traffic conditions across multiple districts in Abuja, predict traffic flow, and recommend the fastest travel routes.

The project demonstrates how **Artificial Intelligence, Data Science, Geospatial Analytics, and Graph Algorithms** can be integrated into a single intelligent transportation system to support smarter mobility and urban planning.

---

# 🌐 Live Application

🔗 https://olonisakin-k-pa.streamlit.app/

---

# 📌 Project Overview

Urban traffic congestion remains one of the biggest challenges facing modern cities.

This project was developed to demonstrate how Artificial Intelligence can support intelligent transportation systems by combining:

- Machine Learning
- GIS Visualization
- Route Optimization
- Interactive Analytics

into a single decision-support platform.

The system currently covers multiple locations across Abuja including:

- Maitama
- Wuse
- Garki
- Berger Junction
- Eagle Square
- Area 10

Users can simulate different traffic conditions, visualize congestion on an interactive GIS map, and identify the fastest route between locations.

---

# 🚀 Key Features

## 🕒 Time-of-Day Simulation

Simulate traffic conditions during:

- Off-Peak
- Normal Traffic
- Rush Hour

---

## 🔍 Smart Traffic Filters

Filter traffic routes by:

- District
- Traffic Level (Light / Moderate / Heavy)

---

## 🤖 Machine Learning Prediction

A **Random Forest Regressor** predicts traffic speed using:

- Route Length
- Adjusted Travel Time

---

## 📊 Model Performance Dashboard

Displays key evaluation metrics including:

- R² Score
- Mean Absolute Error (MAE)

---

## 🔄 Route Optimization

Uses the **NetworkX Shortest Path Algorithm** to determine:

- Fastest route
- Estimated Travel Time (ETA)

---

## 🗺️ Interactive GIS Traffic Map

Built with **PyDeck**, the GIS dashboard displays:

- Road network visualization
- Traffic congestion colours
- Route labels
- Highlighted optimal routes

---

## 🧭 Traffic Legend

🟢 Light Traffic

🟡 Moderate Traffic

🔴 Heavy Traffic

---

# 📸 Application Screenshots

## 🖥️ Dashboard

![Dashboard](assets/Dashboard.png)

---

## 🗺️ GIS Traffic Map

Traffic Map.png

---

# 📍 GIS Traffic Map Overview

The interactive GIS Traffic Map enables users to explore traffic conditions across multiple districts in Abuja.

### 🔍 Sidebar Filters

Users can filter the dashboard by:

- District
- Traffic Level

making it easy to focus on specific areas.

---

### 🗺️ Route Visualization

Each coloured line represents a road segment connecting two locations.

The labels displayed on each segment indicate the estimated travel time.

Examples:

- **181 sec ≈ 3 minutes**
- **674 sec ≈ 11 minutes**

---

### 🚦 Traffic Colours

🟢 Green — Light Traffic

🟡 Yellow — Moderate Traffic

🔴 Red — Heavy Traffic

---

### 📌 Benefits

The GIS dashboard helps users:

- Identify congested roads
- Compare travel times
- Select faster routes
- Support transportation planning
- Improve mobility decisions

---

# 🧠 Machine Learning Model

## Algorithm

**Random Forest Regressor**

### Input Features

- Route Length (km)
- Adjusted Travel Time (seconds)

### Predicted Output

- Average Travel Speed (km/h)

---

# 📊 Model Performance & Key Learning

This project was developed as a **prototype** to demonstrate the integration of **Machine Learning, GIS visualization, route optimization, and interactive analytics** into a complete intelligent transportation platform.

One interesting observation during development was that the model's **R² score changed slightly between application runs.**

After investigating, I found that this was **not caused by an error in the code**. The variation occurred because the model was retrained each time using a different random split of the available data into training and testing sets. With a relatively small demonstration dataset, different train-test splits naturally produce different evaluation results.

This reinforced an important lesson in Machine Learning:

> **Model performance depends not only on selecting an appropriate algorithm but also on the quality, quantity, and representativeness of the training data, as well as a reproducible evaluation strategy.**

Although the predictive model is still being refined, the project successfully demonstrates the integration of:

- Machine Learning
- GIS Mapping
- Route Optimization
- Interactive Dashboards
- Traffic Analytics
- Cloud Deployment

The next phase of development will focus on:

- Expanding the traffic dataset
- Using a fixed random seed (`random_state`) for reproducible experiments
- Comparing multiple regression algorithms
- Improving feature engineering
- Increasing predictive accuracy
- Integrating real-time traffic data

This project demonstrates not only a machine learning model but the design of an end-to-end intelligent transportation system.

---

# 🛠️ Technology Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- NetworkX
- PyDeck
- Machine Learning
- GIS & Geospatial Analytics

---

# 📂 Project Structure

```text
Multi-Districts-Smart-Traffic-Intelligence-System-Abuja/
│── assets/
│   ├── Dashboard.png
│   ├── Traffic Map.png
│── dad8.py
│── requirements.txt
│── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/kola56de/Multi-Districts-Smart-Traffic-Intelligence-System-Abuja.git

cd Multi-Districts-Smart-Traffic-Intelligence-System-Abuja
```

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Run the Application

```bash
streamlit run dad8.py
```

---

# 🎯 Use Cases

- Intelligent Transportation Systems
- Smart Mobility
- Urban Traffic Monitoring
- Route Optimization
- GIS Transportation Analytics
- Smart City Planning
- Traffic Flow Prediction
- Decision Support Systems

---

# 📈 Future Improvements

- Google Maps Traffic API Integration
- AI Congestion Forecasting
- Accident Detection Alerts
- Public Transport Route Integration
- GPS-Based Vehicle Tracking
- Power BI Executive Dashboard
- Mobile Application
- Larger Training Dataset (5,000+ Traffic Records)

---

# 👨‍💻 Author

## **Engr. Dr. Kolade Olonisakin, FNSE**

**Civil Engineer | Data Scientist | Machine Learning Engineer | AI Engineer | Transportation & GIS Analytics**

🌍 **Portfolio**

https://olonisakin-emmanuel.github.io/OlonisakinEmmanuel.github.io/

💼 **LinkedIn**

https://www.linkedin.com/in/engr-dr-kolade-olonisakin-fnse/

💻 **GitHub**

https://github.com/kola56de

---

# ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.

Feedback, suggestions, and collaboration opportunities are always welcome.
