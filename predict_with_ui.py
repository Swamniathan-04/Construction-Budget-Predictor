import streamlit as st
import pandas as pd
from ml_model import ConstructionBudgetPredictor

st.set_page_config(page_title="Construction Budget Predictor", layout="centered")
st.title("🏗️ Construction Budget Predictor")
st.write("Enter your project details below to estimate the construction budget.")

# Feature input widgets
def user_input_features():
    project_area_sqft = st.number_input("Project area (sqft)", min_value=100.0, max_value=100000.0, value=5000.0, step=100.0)
    num_floors = st.number_input("Number of floors", min_value=1, max_value=50, value=3, step=1)
    construction_type = st.selectbox("Construction type", ["residential", "commercial", "industrial"])
    location_urban = st.radio("Is the location urban?", ["Yes", "No"])
    complexity_score = st.slider("Complexity score", 1.0, 10.0, 5.0, 0.1)
    materials_quality = st.selectbox("Materials quality", ["low", "medium", "high"])
    labor_cost_per_sqft = st.number_input("Labor cost per sqft", min_value=10.0, max_value=500.0, value=120.0, step=1.0)
    permits_and_fees = st.number_input("Permits and fees", min_value=0.0, max_value=100000.0, value=15000.0, step=100.0)
    site_preparation_cost = st.number_input("Site preparation cost", min_value=0.0, max_value=200000.0, value=25000.0, step=100.0)
    utilities_cost = st.number_input("Utilities cost", min_value=0.0, max_value=50000.0, value=12000.0, step=100.0)
    project_duration_months = st.number_input("Project duration (months)", min_value=1.0, max_value=60.0, value=12.0, step=1.0)

    # Map categorical to numeric
    construction_type_map = {'residential': 0, 'commercial': 1, 'industrial': 2}
    materials_quality_map = {'low': 0, 'medium': 1, 'high': 2}
    location_urban_val = 1 if location_urban == "Yes" else 0

    features = {
        'project_area_sqft': project_area_sqft,
        'num_floors': num_floors,
        'construction_type': construction_type_map[construction_type],
        'location_urban': location_urban_val,
        'complexity_score': complexity_score,
        'materials_quality': materials_quality_map[materials_quality],
        'labor_cost_per_sqft': labor_cost_per_sqft,
        'permits_and_fees': permits_and_fees,
        'site_preparation_cost': site_preparation_cost,
        'utilities_cost': utilities_cost,
        'project_duration_months': project_duration_months
    }
    return features

# Main app logic
predictor = ConstructionBudgetPredictor()
predictor.load_model()

with st.form("prediction_form"):
    features = user_input_features()
    submitted = st.form_submit_button("Predict Budget")

if submitted:
    df = pd.DataFrame([features])
    prediction = predictor.predict(df)
    st.success(f"Estimated Construction Budget: ${prediction[0]:,.2f}") 