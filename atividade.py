import pandas as pd
import streamlit as st

st.title('Análise do Instagram de João Campos')
st.write("AS 10 PUBLICAÇÕES COM MAIOR ENGAJAMENTO")

interactions = df[['Link', 'Post Created Date', 'Total Interactions']]
interactions.sort_values(by='Total Interactions', ascending=False).head(10)
