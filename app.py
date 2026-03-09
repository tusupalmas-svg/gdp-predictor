import streamlit as st
import pandas as pd
import joblib

model = joblib.load("gdp_model.joblib")

st.title("US GDP per Capita Predictor")

unrate = st.number_input("Unemployment Rate (%)", value=5.0)
confidence = st.number_input("Consumer Confidence Index", value=100.0)
ppi = st.number_input("PPI Construction Materials", value=150.0)
cpi = st.number_input("CPI", value=250.0)
inflation = st.number_input("Inflation (%)", value=3.0)
mortgage = st.number_input("Mortgage Rate (%)", value=5.0)
income = st.number_input("Median Household Income", value=70000.0)
bond = st.number_input("Corporate Bond Yield (%)", value=5.0)
supply = st.number_input("Monthly Home Supply", value=6.0)
working_pop = st.number_input("Working Population Share (%)", value=60.0)
real_gdp = st.number_input("Quarterly Real GDP", value=20000.0)
growth = st.number_input("GDP Growth Rate (%)", value=2.0)
house_index = st.number_input("Case Shiller Index", value=200.0)

if st.button("Predict"):

    data = pd.DataFrame([[

        unrate,
        confidence,
        ppi,
        cpi,
        inflation,
        mortgage,
        income,
        bond,
        supply,
        working_pop,
        real_gdp,
        growth,
        house_index

    ]], columns=[

        'UNRATE(%)',
        'CONSUMER CONF INDEX',
        'PPI-CONST MAT.',
        'CPIALLITEMS',
        'INFLATION(%)',
        'MORTGAGE INT. MONTHLY AVG(%)',
        'MED HOUSEHOLD INCOME',
        'CORP. BOND YIELD(%)',
        'MONTHLY HOME SUPPLY',
        '% SHARE OF WORKING POPULATION',
        'QUARTERLY REAL GDP',
        'QUARTERLY GDP GROWTH RATE (%)',
        'CSUSHPISA'

    ])

    prediction = model.predict(data)

    st.success(f"GDP per Capita prediction: ${prediction[0]:,.2f}")
    