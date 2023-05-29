import pandas as pd
import csv
import streamlit as st

dataframe = pd.read_csv('JoaoInsta.csv')

st.title('Análise do Instagram de João Campos')

st.write("AS 10 PUBLICAÇÕES MAIS ENGAJADAS")

likes = dataframe[['Link', 'Post Created Date', 'Likes']]
likes.sort_values(by='Likes', ascending=False).head(10)
