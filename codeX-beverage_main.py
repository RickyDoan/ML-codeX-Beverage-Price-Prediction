import streamlit as st
import pandas as pd
from helper_db import preprocessing
from joblib import load

# model = load("artifact/best_model.joblib")
pipline = load("artifact/pipline.joblib")
pipline_rdf = load("artifact/pipline_rdf.joblib")
df = load("artifact/dataframe.joblib")

# Streamlit App
st.title("CodeX Beverage : Price Prediction")

# Using sorted unique values for each input
age_options = list(range(18, 71))  # Specific range for 'age'
gender_options = sorted(df['gender'].unique())
zone_options = sorted(df['zone'].unique())
occupation_options = sorted(df['occupation'].unique())
income_levels_options = sorted(df['income_levels'].unique())
consume_frequency_options = sorted(df['consume_frequency(weekly)'].unique())
current_brand_options = sorted(df['current_brand'].unique())
consumption_size_options = sorted(df['preferable_consumption_size'].unique())
awareness_options = sorted(df['awareness_of_other_brands'].unique())
reasons_options = sorted(df['reasons_for_choosing_brands'].unique())
flavor_options = sorted(df['flavor_preference'].unique())
purchase_channel_options = sorted(df['purchase_channel'].unique())
packaging_options = sorted(df['packaging_preference'].unique())
health_concerns_options = sorted(df['health_concerns'].unique())
situations_options = sorted(df['typical_consumption_situations'].unique())

# Row 1: Four standard inputs
col1, col2, col3, col4 = st.columns(4)
with col1:
    age = st.selectbox("Age", age_options)
with col2:
    gender = st.selectbox("Gender", gender_options)
with col3:
    zone = st.selectbox("Zone", zone_options)
with col4:
    occupation = st.selectbox("Occupation", occupation_options)

# Row 6: Four standard inputs
col1, col2, col3, col4 = st.columns(4)
with col1:
    purchase_channel = st.selectbox("Purchase Channel", purchase_channel_options)
with col2:
    packaging_preference = st.selectbox("Packaging Preference", packaging_options)
with col3:
    current_brand = st.selectbox("Current Brand", current_brand_options)

with col4:
    income_levels = st.selectbox("Income Levels", income_levels_options)

# Row 2: Longer input spans two columns
col1, col2 = st.columns(2)
with col1:
    typical_consumption_situations = st.selectbox("Typical Consumption Situations", situations_options)
with col2:
    consume_frequency = st.selectbox("Consume Frequency (Weekly)", consume_frequency_options)

# Row 3: Another set of two longer inputs
col1, col2 = st.columns(2)
with col1:
    health_concerns = st.selectbox("Health Concerns", health_concerns_options)
with col2:
    preferable_consumption_size = st.selectbox("Preferable Consumption Size", consumption_size_options)

# Row 4: Two longer inputs
col1, col2 = st.columns(2)
with col1:
    awareness_of_other_brands = st.selectbox("Awareness of Other Brands", awareness_options)
with col2:
    reasons_for_choosing_brands = st.selectbox("Reasons for Choosing Brands", reasons_options)

# Row 5: One long input spans full row
flavor_preference = st.selectbox("Flavor Preference", flavor_options)


def price_range(predict):
    if predict == 1:
        return "50-100"
    if predict == 2:
        return "100-150"
    if predict == 3:
        return "150-200"
    if predict == 4:
        return "200-250"
    # y = y.map({'50-100': 1, '100-150': 2, '150-200': 3, '200-250': 4})
# Submit Button
if st.button("Predict Price"):
    # Collecting input values into a dictionary
    input_data = {
        'age': age,
        'gender': gender,
        'zone': zone,
        'occupation': occupation,
        'income_levels': income_levels,
        'consume_frequency(weekly)': consume_frequency,
        'current_brand': current_brand,
        'preferable_consumption_size': preferable_consumption_size,
        'awareness_of_other_brands': awareness_of_other_brands,
        'reasons_for_choosing_brands': reasons_for_choosing_brands,
        'flavor_preference': flavor_preference,
        'purchase_channel': purchase_channel,
        'packaging_preference': packaging_preference,
        'health_concerns': health_concerns,
        'typical_consumption_situations': typical_consumption_situations
    }

    df = pd.DataFrame(input_data, index=[0])
    # st.write(pipline)
    # st.write(pipline_rdf)
    predict = int(pipline_rdf.predict(df))
    call_price_range = price_range(predict)
    st.success(f"Price Range Prediction: {call_price_range}")
    st.balloons()
