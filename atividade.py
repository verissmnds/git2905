import streamlit as st 
import pandas as pd

df = pd.read_csv('dados.csv')

st.title('analise do instagram de joao campos')
st.write('as 10 publicacoes com maior engajamento')

likes = df[['link','Post Created Date', 'Likes']]
likes = likes.sort_values(by='Likes', ascending=False).head(10)
st.dataframe(likes)
