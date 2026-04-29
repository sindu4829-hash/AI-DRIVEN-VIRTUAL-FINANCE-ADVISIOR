import streamlit as st
from predict import predict_risk
from utils import get_recommendation

st.title("💰 AI Financial Advisor")

# User Inputs
age = st.slider("Age", 18, 60, 25)

goal = st.selectbox("Investment Goal",
                    ["Short-term", "Long-term"])

goal_val = 1 if goal == "Short-term" else 2

savings = st.number_input("Monthly Savings (INR)", min_value=1000)

# Button
if st.button("Get Advice"):

    risk = predict_risk(age, goal_val, savings)
    advice = get_recommendation(risk, savings)

    st.subheader("📊 Result")
    st.write(f"Risk Profile: {risk}")
    st.success(advice)