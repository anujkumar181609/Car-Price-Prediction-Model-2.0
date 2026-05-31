#importing libraries
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

#page setup
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #111827);
    color: white;
}

.title-text {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #60a5fa;
}

.subtitle-text {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 25px;
}

[data-testid="stSidebar"] {
    background: #0b1220;
}

.prediction-card {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
}

div[data-baseweb="select"],
div[data-testid="stNumberInput"],
div[data-testid="stSlider"] {
    background-color: #1e293b;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("🚘 Project Information")

    st.markdown("""
### Objective
Predict the resale value of used cars using machine learning.

### Algorithm Used
**Random Forest Regressor**

### Input Features
- Company
- Model Name
- Year
- Kilometers Driven
- Fuel Type

### Why Random Forest?
- High Accuracy
- Handles Non-Linearity
- Less Overfitting
- Strong Performance on Tabular Data
""")

    st.markdown("---")
    st.caption("Built with Streamlit & Machine Learning")



# importing dataset
BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "clean_car_price_data.csv"
df = pd.read_csv(csv_path)

# importing model
model_path = BASE_DIR / "car_price_rf_model.pkl"
model= joblib.load(open(model_path, 'rb'))

#heading and subheading
st.markdown('<div class="title-text">🚗 Car Price Prediction Model</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">AI Powered Used Car Price Estimator</div>', unsafe_allow_html=True)

col1,col2=st.columns(2)


with col1:
    company= st.selectbox("Company", df['company'].unique(),index= None, placeholder= "Select a Company")
    filtered_models= df[df['company']==company]['name'].unique()
    name= st.selectbox("Car Model", index=None, options= filtered_models, placeholder= "Select a Car Model")
    year= st.slider("Year", 1995,2020)

with col2:
    kms=st.number_input("Kms Driven", min_value=0)
    filtered_fuels= df[(df['company']==company) & (df['name']==name)]['fuel_type'].unique()
    fuel= st.selectbox("Fuel Type", filtered_fuels)
    
    

if st.button("🚀 Predict Price", use_container_width=True):

    input_df= pd.DataFrame(
        [[name,company,year,kms,fuel]],
        columns=['name','company','year','kms_driven','fuel_type']
    )

    prediction= model.predict(input_df).item()

    st.markdown(f"""
    <div class="prediction-card">
        <h2 style="text-align:center;">Predicted Price</h2>
        <h1 style="text-align:center;color:#22c55e;">
            ₹ {prediction:,.2f}
        </h1>
    </div>
    """, unsafe_allow_html=True)
