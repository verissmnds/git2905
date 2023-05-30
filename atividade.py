import pandas as pd
import streamlit as st

st.title('Análise do Instagram de João Campos')
st.write("AS 10 PUBLICAÇÕES COM MAIOR ENGAJAMENTO")

likes = df[['Link', 'Post Created Date', 'Likes']]
likes.sort_values(by='Likes', ascending=False).head(10)
