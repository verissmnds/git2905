import pandas as pd
import csv
import streamlit as st

arquivo = open('JoaoInsta.csv')
print(arquivo)

st.title('Análise do Instagram de João Campos')

st.write("AS 10 PUBLICAÇÕES MAIS ENGAJADAS")

likes = arquivo[['Link', 'Post Created Date', 'Likes']]
likes.sort_values(by='Likes', ascending=False).head(10)
