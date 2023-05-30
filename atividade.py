import pandas as pd
import streamlit as st 

st.title('CSV Viewer')
dados = pd.read_csv('dados.csv')
st.dataframe(dados)
