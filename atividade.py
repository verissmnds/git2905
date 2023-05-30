import streamlit as st 
import pandas as pd

df = pd.read_csv('Joao.csv.csv')

st.title('Análise do Instagram de João Campos')
st.write('As 10 publicações com maior engajamento')

likes = df[['link','Post Created Date', 'Likes']]
likes = likes.sort_values(by='Likes', ascending=False).head(10)
st.dataframe(likes)
