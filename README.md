# 🚦 Multi-Districts Smart Traffic Intelligence System (Abuja) 

An AI-powered traffic intelligence platform built with **Streamlit**, **Machine Learning**, **GIS Mapping**, and **Route Optimization Algorithms** to analyze road traffic conditions across multiple Abuja districts, predict traffic flow, and recommend the fastest routes.

🔗 **Live App:** https://olonisakin-k-pa.streamlit.app/

---

## 📌 Project Overview

Urban traffic congestion remains a major challenge in developing smart cities. This project provides an intelligent traffic monitoring and route optimization solution for Abuja using historical road data, predictive analytics, and interactive mapping.

The system covers multiple districts including:

- Maitama  
- Wuse  
- Garki  
- Area 10  
- Eagle Square  
- Berger Axis  

Users can simulate traffic conditions, analyze congestion, and identify the best routes based on travel time.

---

## 🚀 Features

### 🕒 Time of Day Simulation

Simulate traffic patterns based on:

- Off-Peak  
- Normal  
- Rush Hour  

### 🔍 Smart Filters

Filter traffic routes by:

- District  
- Traffic Level (Light / Moderate / Heavy)

### 🤖 Machine Learning Prediction

Uses **Random Forest Regressor** to evaluate traffic speed performance using:

- Route Length  
- Adjusted Travel Time  

### 📊 Model Performance

Displays:

- **R² Score**
- **Mean Absolute Error (MAE)**

### 🔄 Route Optimization

Uses **NetworkX shortest path algorithm** to determine:

- Fastest route between two locations  
- Estimated travel time (ETA)

### 🗺️ GIS Traffic Map

Interactive traffic map powered by **PyDeck** showing:

- Live route lines  
- Traffic congestion colors  
- Route labels  
- Highlighted best path

### 🧭 Traffic Legend

- 🟢 Light Traffic  
- 🟡 Moderate Traffic  
- 🔴 Heavy Traffic  

---

## 🖼️ App Screenshots

### Dashboard

![Dashboard](assets/Dashboard.png)

### Traffic Map

![Traffic Map](assets/Traffic%20Map.png)

---

## 📝 Traffic Map Explanation

This dashboard includes an interactive **GIS Traffic Map** that visualizes real-time simulated traffic conditions across selected Abuja districts.

### 🔍 Sidebar Filters

Users can filter the map by:

- **District** (e.g., Maitama, Wuse)  
- **Traffic Level** (Light, Moderate, Heavy)

This allows focused traffic analysis for specific locations.

### 🗺️ Route Map Interpretation

Colored route lines represent roads connecting key locations.  
Each route displays estimated travel time in **seconds**.

Examples:

- **181 sec** ≈ 3 minutes  
- **674 sec** ≈ 11 minutes  

### 🚦 Traffic Color Legend

- 🟢 **Green** = Light Traffic  
- 🟡 **Yellow** = Moderate Traffic  
- 🔴 **Red** = Heavy Traffic  

### 📌 Benefits of the Map

- Detect congested roads quickly  
- Compare route travel times  
- Support route optimization  
- Assist smart city planning  
- Improve transport decision-making  

### 🧠 Summary

The map functions like a mini **AI-powered Google Maps Traffic System for Abuja**, combining GIS visualization and traffic intelligence.

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- PyDeck  
- NetworkX  
- Scikit-learn  
- Random Forest Regression  

---

## 📂 Project Structure

```bash
Multi-Districts-Smart-Traffic-Intelligence-System-Abuja/
│── assets/
│   ├── Dashboard.png
│   └── Traffic Map.png
│── dad8.py
│── requirements.txt
```
---
⚙️ Installation & Setup
1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/Multi-Districts-Smart-Traffic-Intelligence-System-Abuja.git
cd Multi-Districts-Smart-Traffic-Intelligence-System-Abuja
```
---
2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
---
3️⃣ Run App
```bash
streamlit run dad8.py
```
---
## 📌 Use Cases

- Smart Mobility Systems  
- Urban Traffic Monitoring  
- Route Optimization  
- Smart City Planning  
- Traffic Flow Prediction  
- GIS Transportation Analytics  

## 📈 Future Improvements

- Real-time Google Maps Traffic API  
- Accident Detection Alerts  
- Public Transport Route Integration  
- AI Congestion Forecasting  
- Power BI Executive Dashboard  
- Mobile App Version  

## 👨‍💻 Author

**Kolade Olonisakin**  
Data Scientist | Machine Learning Engineer | AI Enthusiast  

## ⭐ Support

If you like this project, kindly **star the repository** and share.
