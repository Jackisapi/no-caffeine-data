import streamlit as st
from pandas import read_csv

data = st.file_uploader("Upload your data in a csv please ", type='.csv')

while data is None:
    continue

data = read_csv(data)

st.write(data)

pressure_chart = st.line_chart(data=data, x="date", y="blood_pressure")

concentration_chart = st.line_chart(data=data, x="date", y="heart_rate")

heart_rate = st.line_chart(data=data, x="date", y="concentration")
