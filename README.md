# 🌿 Travel Product Prediction System

A machine learning-powered web application built using **Streamlit** that predicts whether a customer will take a travel product or not. It includes prediction, analytics dashboard, and MySQL database storage with interactive visualizations.

---

## 🚀 Features
- 🧠 ML-based prediction (Taken / Not Taken)
- 📊 Interactive dashboard with filters
- 📈 Probability visualization (bar chart, pie chart, histogram)
- 🗄️ MySQL database integration (auto save predictions)
- 🎨 Modern UI with custom styling
- 🔎 Sidebar filters for analysis

---

## 🏗️ Tech Stack
- Python 🐍  
- Streamlit 🎈  
- Pandas 📊  
- Scikit-learn 🤖  
- MySQL 🗄️  
- Plotly 📈  
- Joblib 💾  

---

## 🖥️ Application Pages

### 🏠 Home
- App introduction
- Navigation to prediction page

### ✈️ Prediction Page
- Input customer details
- Predict result (Taken / Not Taken)
- Show probability graph
- Auto-save prediction in database

### 📊 Data Page
- Displays all stored predictions from MySQL

### 📈 Dashboard Page
- Filters:
  - Prediction
  - Gender
  - City Tier
- KPIs:
  - Total predictions
  - Taken count
  - Average probability
  - High confidence predictions
- Visualizations:
  - Pie chart (distribution)
  - Histogram (probability)

---

## 🗄️ Database Table: `predictions`

- Age  
- TypeofContact  
- CityTier  
- DurationOfPitch  
- Occupation  
- Gender  
- NumberOfFollowups  
- ProductPitched  
- PreferredPropertyStar  
- MaritalStatus  
- NumberOfTrips  
- Passport  
- PitchSatisfactionScore  
- OwnCar  
- Designation  
- MonthlyIncome  
- TotalVisiting  
- Prediction  
- Probability  

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py

📊 Output
Prediction: Taken / Not Taken
Probability Score (0–1)
Stored automatically in database
Interactive dashboard visualization

🎯 Future Enhancements
User login system
Model retraining module
Export reports (PDF/Excel)
Cloud deployment (AWS / Streamlit Cloud)

👨‍💻 Author
Developed by Snehal Raghoji
