import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Bird observations and its influences")

st.write("Welcome to the website")

st.subheader("Data check")

try:
   
    df = pd.read_csv("RQ_1/Hamburg_air_pollution_statistics_2021-2025.csv")
    st.success("CSV found!")
    st.write(df.head())
except:
    st.error("No CSV found. Please check the file path.")
   