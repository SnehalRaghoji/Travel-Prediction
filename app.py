# import streamlit as st
# import pandas as pd
# import joblib

# import mysql.connector

# # DB Connection

# def get_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Shona@18",
#         database="ml_app",
#     )


# def save_to_db(data,prediction,probability):
#     conn=get_connection()
#     cursor=conn.cursor()


#     query = """
#         INSERT INTO predictions (
#         Age, TypeofContact, CityTier, DurationOfPitch, Occupation, Gender,
#         NumerOfFollowups, ProductPitched, PreferredPropertyStar, MaritalStatus,
#         NumberOfTrips, Passport, PitchSatisfactionScore, OwnCar, Designation,
#         MnothlyIncome, TotalVisiting, Prediction, Probability
#     ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
#     """

#     values = (
#     int(data["Age"][0]),
#     str(data["TypeofContact"][0]),
#     int(data["CityTier"][0]),
#     int(data["DurationOfPitch"][0]),
#     str(data["Occupation"][0]),
#     str(data["Gender"][0]),
#     int(data["NumberOfFollowups"][0]),
#     str(data["ProductPitched"][0]),
#     int(data["PreferredPropertyStar"][0]),
#     str(data["MaritalStatus"][0]),
#     int(data["NumberOfTrips"][0]),
#     int(data["Passport"][0]),
#     int(data["PitchSatisfactionScore"][0]),
#     int(data["OwnCar"][0]),
#     str(data["Designation"][0]),
#     int(data["MonthlyIncome"][0]),
#     int(data["TotalVisiting"][0]),
#     int(prediction),                         # ✅ FIX
#     float(probability) if probability else None  # ✅ FIX
# )

#     cursor.execute(query, values)
#     conn.commit()
#     conn.close()

# ############################################################

# # Load model and preprocessor
# model = joblib.load("model.joblib")
# preprocessor = joblib.load("preprocessor.joblib")

# # Page config
# st.set_page_config(page_title="Product Taken Prediction", layout="centered")

# st.title("🧳 Product Taken Prediction App")
# st.write("Enter customer details to predict whether the product will be taken or not.")

# st.markdown("---")

# # =========================
# # Input fields
# # =========================

# Age = st.number_input("Age", min_value=18, max_value=100, value=30)

# TypeofContact = st.selectbox(
#     "Type of Contact",
#     ["Self Enquiry", "Company Invited"]
# )

# CityTier = st.selectbox("City Tier", [1, 2, 3])

# DurationOfPitch = st.number_input(
#     "Duration Of Pitch (minutes)", min_value=0, max_value=300, value=30
# )

# Occupation = st.selectbox(
#     "Occupation",
#     ["Salaried", "Small Business", "Large Business", "Free Lancer"]
# )

# Gender = st.selectbox("Gender", ["Male", "Female"])

# NumberOfFollowups = st.number_input(
#     "Number Of Followups", min_value=0, max_value=20, value=2
# )

# ProductPitched = st.selectbox(
#     "Product Pitched",
#     ["Basic", "Standard", "Deluxe", "Super Deluxe", "King"]
# )

# PreferredPropertyStar = st.selectbox(
#     "Preferred Property Star", [3, 4, 5]
# )

# MaritalStatus = st.selectbox(
#     "Marital Status",
#     ["Unmarried", "Married", "Divorced"]
# )

# NumberOfTrips = st.number_input(
#     "Number Of Trips", min_value=0, max_value=50, value=2
# )

# Passport = st.selectbox("Passport", [0, 1])

# PitchSatisfactionScore = st.slider(
#     "Pitch Satisfaction Score", min_value=1, max_value=5, value=3
# )

# OwnCar = st.selectbox("Own Car", [0, 1])

# Designation = st.selectbox(
#     "Designation",
#     ["Executive", "Manager", "Senior Manager", "AVP", "VP"]
# )

# MonthlyIncome = st.number_input(
#     "Monthly Income", min_value=0, value=50000
# )

# TotalVisiting = st.number_input(
#     "Total Visiting", min_value=0, max_value=50, value=2
# )

# # =========================
# # Prediction
# # =========================

# if st.button("🔍 Predict"):
#     input_data = pd.DataFrame({
#         "Age": [Age],
#         "TypeofContact": [TypeofContact],
#         "CityTier": [CityTier],
#         "DurationOfPitch": [DurationOfPitch],
#         "Occupation": [Occupation],
#         "Gender": [Gender],
#         "NumberOfFollowups": [NumberOfFollowups],
#         "ProductPitched": [ProductPitched],
#         "PreferredPropertyStar": [PreferredPropertyStar],
#         "MaritalStatus": [MaritalStatus],
#         "NumberOfTrips": [NumberOfTrips],
#         "Passport": [Passport],
#         "PitchSatisfactionScore": [PitchSatisfactionScore],
#         "OwnCar": [OwnCar],
#         "Designation": [Designation],
#         "MonthlyIncome": [MonthlyIncome],
#         "TotalVisiting": [TotalVisiting]
#     })

#     X_processed = preprocessor.transform(input_data)
#     prediction = model.predict(X_processed)[0]

#     prob = None
#     if hasattr(model, "predict_proba"):
#         prob = model.predict_proba(X_processed)[0][1]
#         st.info(f"📊 Probability: {prob:.2f}")

#     if prediction == 1:
#         st.success("✅ Product WILL BE TAKEN")
#     else:
#         st.error("❌ Product WILL NOT BE TAKEN")

#     # ✅ SAVE TO DATABASE
#     save_to_db(input_data, prediction, prob)

# def fetch_data():
#     conn = get_connection()
#     df = pd.read_sql("SELECT * FROM predictions ORDER BY id DESC", conn)
#     conn.close()
#     return df

# st.markdown("## 📂 Stored Predictions")

# if st.button("📊 View Saved Data"):
#     df = fetch_data()
#     st.dataframe(df)

# st.markdown("---")
# st.caption("ML Model Prediction using Streamlit")








import streamlit as st
import pandas as pd
import joblib
import mysql.connector
import plotly.graph_objects as go
import plotly.express as px

# =========================
# Page Config
# =========================
st.set_page_config(page_title="Travel Product Prediction", layout="wide")

# =========================
# Custom CSS (READABILITY + GRAPH FIX ONLY)
# =========================
st.markdown("""
<style>

/* Background */
.stApp {
    background: url('https://images.unsplash.com/photo-1501785888041-af3ef285b470');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white;
}

/* Headings */
h1, h2, h3 {
    text-align: center;
    color: #FFD54F;
    font-weight: 700;
}

/* Sidebar readability */
section[data-testid="stSidebar"] {
    background: rgba(0,0,0,0.25) !important;
}

section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] p {
    color: #FFFFFF !important;
    font-weight: 600;
}

/* 🔥 Prediction page labels visibility */
div[data-testid="stNumberInput"] label,
div[data-testid="stSelectbox"] label,
div[data-testid="stSlider"] label {
    color: #FFEB3B !important;
    font-weight: 700;
}

/* 🔥 Sidebar filter title visibility */
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #00FFD0 !important;
    font-weight: 800;
}

/* Metric cards */
.metric-card {
    background: rgba(255,255,255,0.08);
    padding: 16px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.15);
}

.metric-title {
    color: #A7FFEB;
    font-size: 14px;
}

.metric-value {
    color: #FFD54F;
    font-size: 24px;
    font-weight: bold;
}

.stButton>button {
    background: linear-gradient(90deg, #43cea2, #185a9d);
    color: white;
    border-radius: 14px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# =========================
# DB Connection
# =========================
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shona@18",
        database="ml_app",
    )

# =========================
# Load Model
# =========================
model = joblib.load("model.joblib")
preprocessor = joblib.load("preprocessor.joblib")

# =========================
# Save Prediction
# =========================
def save_prediction(input_data, prediction, probability):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO predictions (
        Age, TypeofContact, CityTier, DurationOfPitch, Occupation, Gender,
        NumberOfFollowups, ProductPitched, PreferredPropertyStar,
        MaritalStatus, NumberOfTrips, Passport, PitchSatisfactionScore,
        OwnCar, Designation, MonthlyIncome, TotalVisiting,
        Prediction, Probability
    ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    clean_values = []
    for v in list(input_data.values()):
        if hasattr(v, "item"):
            v = v.item()
        clean_values.append(v)

    if hasattr(prediction, "item"):
        prediction = prediction.item()

    if hasattr(probability, "item"):
        probability = probability.item()

    clean_values += [prediction, float(probability)]

    cursor.execute(query, clean_values)
    conn.commit()
    conn.close()

# =========================
# Navigation
# =========================
if "page" not in st.session_state:
    st.session_state.page = "home"

col_nav1, col_nav2, col_nav3, col_nav4 = st.columns([5,1,1,1])
with col_nav2:
    if st.button("🏠 Home"):
        st.session_state.page = "home"
with col_nav3:
    if st.button("📊 Data"):
        st.session_state.page = "data"
with col_nav4:
    if st.button("📈 Dashboard"):
        st.session_state.page = "dashboard"

# =========================
# HOME
# =========================
if st.session_state.page == "home":
    st.title("🌿 Travel Prediction System")
    if st.button("🚀 Start Prediction"):
        st.session_state.page = "prediction"

# =========================
# PREDICTION
# =========================
elif st.session_state.page == "prediction":
    st.title("✈️ Prediction Page")

    col1, col2 = st.columns([1,1])

    with col1:
        Age = st.number_input("Age", 18, 100, 30)
        TypeofContact = st.selectbox("Type of Contact", ["Self Enquiry", "Company Invited"])
        CityTier = st.selectbox("City Tier", [1, 2, 3])
        DurationOfPitch = st.number_input("Duration Of Pitch", 0, 300, 30)
        Occupation = st.selectbox("Occupation", ["Salaried", "Small Business", "Large Business", "Free Lancer"])
        Gender = st.selectbox("Gender", ["Male", "Female"])
        NumberOfFollowups = st.number_input("Number Of Followups", 0, 20, 2)
        ProductPitched = st.selectbox("Product Pitched", ["Basic", "Standard", "Deluxe", "Super Deluxe", "King"])
        PreferredPropertyStar = st.selectbox("Preferred Property Star", [3, 4, 5])

    with col2:
        MaritalStatus = st.selectbox("Marital Status", ["Unmarried", "Married", "Divorced"])
        NumberOfTrips = st.number_input("Number Of Trips", 0, 50, 2)
        Passport = st.selectbox("Passport", [0, 1])
        PitchSatisfactionScore = st.slider("Pitch Satisfaction Score", 1, 5, 3)
        OwnCar = st.selectbox("Own Car", [0, 1])
        Designation = st.selectbox("Designation", ["Executive", "Manager", "Senior Manager", "AVP", "VP"])
        MonthlyIncome = st.number_input("Monthly Income", 0, 1000000, 50000)
        TotalVisiting = st.number_input("Total Visiting", 0, 50, 2)

    if st.button("🔍 Predict"):
        input_data = {
            "Age": Age,
            "TypeofContact": TypeofContact,
            "CityTier": CityTier,
            "DurationOfPitch": DurationOfPitch,
            "Occupation": Occupation,
            "Gender": Gender,
            "NumberOfFollowups": NumberOfFollowups,
            "ProductPitched": ProductPitched,
            "PreferredPropertyStar": PreferredPropertyStar,
            "MaritalStatus": MaritalStatus,
            "NumberOfTrips": NumberOfTrips,
            "Passport": Passport,
            "PitchSatisfactionScore": PitchSatisfactionScore,
            "OwnCar": OwnCar,
            "Designation": Designation,
            "MonthlyIncome": MonthlyIncome,
            "TotalVisiting": TotalVisiting
        }

        input_df = pd.DataFrame([input_data])
        X_processed = preprocessor.transform(input_df)

        prediction = model.predict(X_processed)[0]
        prob = model.predict_proba(X_processed)[0][1]

        save_prediction(input_data, prediction, prob)

        st.success("Prediction Done & Saved!")

        # =========================
        # 📊 IMPROVED GRAPH (TAKEN vs NOT TAKEN)
        # =========================
        fig = go.Figure()

        fig.add_trace(go.Bar(
            name="Taken",
            x=["Probability"],
            y=[prob]
        ))

        fig.add_trace(go.Bar(
            name="Not Taken",
            x=["Probability"],
            y=[1 - prob]
        ))

        fig.update_layout(
            title="Probability of Taking Product",
            yaxis_title="Probability",
            barmode="group",
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

# =========================
# DATA
# =========================
elif st.session_state.page == "data":
    st.title("📊 Stored Predictions")

    def fetch_data():
        conn = get_connection()
        df = pd.read_sql("SELECT * FROM predictions ORDER BY id DESC", conn)
        conn.close()
        return df

    if st.button("Load Data"):
        df = fetch_data()
        st.dataframe(df)

# =========================
# DASHBOARD
# =========================
elif st.session_state.page == "dashboard":
    st.title("📈 Interactive Dashboard")

    def fetch_data():
        conn = get_connection()
        df = pd.read_sql("SELECT * FROM predictions", conn)
        conn.close()
        return df

    df = fetch_data()

    if len(df) > 0:

        st.sidebar.header("🔎 Filters")

        pred_filter = st.sidebar.multiselect("Prediction", [0, 1], default=[0, 1])
        gender_filter = st.sidebar.multiselect("Gender", df["Gender"].unique(), default=list(df["Gender"].unique()))
        city_filter = st.sidebar.multiselect("City Tier", df["CityTier"].unique(), default=list(df["CityTier"].unique()))

        df = df[df["Prediction"].isin(pred_filter)]
        df = df[df["Gender"].isin(gender_filter)]
        df = df[df["CityTier"].isin(city_filter)]

        avg_prob = df["Probability"].mean()

        col1, col2, col3, col4 = st.columns(4)

        col1.markdown(f"<div class='metric-card'><div class='metric-title'>Total</div><div class='metric-value'>{len(df)}</div></div>", unsafe_allow_html=True)

        col2.markdown(f"<div class='metric-card'><div class='metric-title'>Taken</div><div class='metric-value'>{len(df[df['Prediction']==1])}</div></div>", unsafe_allow_html=True)

        col3.markdown(f"<div class='metric-card'><div class='metric-title'>Avg Probability</div><div class='metric-value'>{avg_prob:.2f}</div></div>", unsafe_allow_html=True)

        col4.markdown(f"<div class='metric-card'><div class='metric-title'>High Confidence</div><div class='metric-value'>{len(df[df['Probability']>0.8])}</div></div>", unsafe_allow_html=True)

        fig1 = px.pie(df, names="Prediction", title="Prediction Distribution")
        fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig1, use_container_width=True)

        fig2 = px.histogram(df, x="Probability", nbins=20, title="Probability Distribution")
        fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig2, use_container_width=True)

        st.dataframe(df)

    else:
        st.warning("No data available")
