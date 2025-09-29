pip install streamlit
streamlit run app.py

import streamlit as st
import joblib

modelo = joblib.load('model/modelo_sorvete.pkl')

st.title("Previsão de Vendas de Sorvete 🍦")
temp = st.slider("Temperatura do dia (°C)", 15, 40)
venda = modelo.predict([[temp]])
st.write(f"Previsão: {int(venda[0])} sorvetes vendidos")
