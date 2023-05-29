import pandas as pd
import csv

st.title('Análise do Instagram de João Campos')

arquivo = open('JoaoInsta.csv')

st.write("AS 10 PUBLICAÇÕES MAIS ENGAJADAS")

likes = df[['Link', 'Post Created Date', 'Likes']]
likes.sort_values(by='Likes', ascending=False).head(10)
