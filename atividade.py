import csv
import pandas as pd
import streamlit as st

df = pd.read_csv('JoaoCampos (2).csv')
display(df)

st.title('Análise do Instagram de João Campos')
st.write("AS 10 PUBLICAÇÕES COM MAIOR ENGAJAMENTO")

df['Total Interactions'] = df['Total Interactions'].apply(lambda x: x.replace(',', ''))
df['Total Interactions'] = df['Total Interactions'].astype(int)

interactions = df[['Link', 'Post Created Date', 'Total Interactions']]
interactions.sort_values(by='Total Interactions', ascending=False).head(10)
