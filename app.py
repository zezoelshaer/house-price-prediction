import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("model.pkl")

st.title("🏠 House Price Prediction")

Area = st.slider("Carpet Area (sqft)", min_value=100.0, max_value=10000.0, value=1000.0)
Bedrooms = st.slider("Bedrooms", min_value=1, max_value=10, value=2)
Bathroom = st.slider("Bathroom", min_value=1, max_value=10, value=2)
Balcony = st.slider("Balcony", min_value=0, max_value=10, value=1)
Floor = st.slider("Floor (0 = Ground)", min_value=0, max_value=100, value=3)
TotalFloors = st.slider("Total Floors", min_value=1, max_value=100, value=10)

Location = st.selectbox("Location",['faridabad', 'gurgaon', 'new-delhi', 'greater-noida', 'ahmedabad',
       'pune', 'vadodara', 'hyderabad', 'kolkata', 'bangalore', 'chennai',
       'jaipur', 'visakhapatnam', 'zirakpur', 'mohali', 'surat', 'chandigarh',
       'noida', 'ranchi', 'ghaziabad', 'kochi', 'goa', 'thane', 'kanpur',
       'sonipat', 'dehradun', 'lucknow', 'guwahati', 'bhiwadi', 'patna',
       'kalyan', 'vijayawada', 'jamshedpur', 'raipur', 'mumbai', 'coimbatore',
       'panchkula', 'badlapur', 'agra', 'mangalore'])

Furnishing = st.selectbox("Furnishing", [
    "Furnished", "Semi-Furnished", "Unfurnished"
])

if st.button("Predict") :

    if Floor > TotalFloors :
        st.error("Floor can't be higher than Total Floors")

    else :
        input_df = pd.DataFrame(0.0, index=[0], columns = model.feature_names_in_)

        input_df["Carpet Area"] = Area
        input_df["Bedrooms"] = Bedrooms
        input_df["Bathroom"] = Bathroom
        input_df["Balcony"] = Balcony
        input_df["Floor No"] = Floor
        input_df["Total Floors"] = TotalFloors

        if Location in input_df.columns :
            input_df[Location] = 1

        if Furnishing in input_df.columns :
            input_df[Furnishing] = 1

        price = model.predict(input_df)[0]

        if price >= 10000000 :
            st.success(f"Price = {price / 10000000:.2f} Crore ₹")
        else :
            st.success(f"Price = {price / 100000:.1f} Lakh ₹")