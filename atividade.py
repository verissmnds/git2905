import pandas as pd
import streamlit as st 

st.title('Análise do Instagram de João Campos')
st.write('Analisando o engajamento da Campanha Permanente do prefeito João Campos')

dados = pd.read_csv('Joao.csv.csv')
st.dataframe(dados)
