import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title="VG Sales Dashboard.",page_icon="🎮",
    layout="centered",menu_items={
        'About': 'A Dashboard for Video Game Sales Analysis.'
    })

st.title('Video Games Sales Analysis...🎮')




image = Image.open('sales.png')
st.image(image)

st.markdown("---")


st.cache_data()
df = pd.read_csv('vgsales.csv')
df.dropna( axis=0, how="any", subset=['Year','Publisher'], inplace=True)


st.header('Data exploration.')

st.markdown("""
            
            ---
#### *※ Columns in the data along with their description.*

- `Rank:` The ranking position of the game in terms of global sales.
- `Name:` The name of the video game.
- `Platform:` The gaming platform (console or system) on which the game was released.
- `Year:` The year when the game was released.
- `Genre:` The genre or category of the game (e.g., action, adventure, sports).
- `Publisher:` The company or entity responsible for publishing and distributing the game.
- `NA_Sales:` Sales of the game in North America (in millions of units).
- `EU_Sales:` Sales of the game in Europe (in millions of units).
- `JP_Sales:` Sales of the game in Japan (in millions of units).
- `Other_Sales:` Sales of the game in regions other than North America, Europe, and Japan (in millions of units).
- `Global_Sales:` Total global sales of the game (sum of sales across all regions, in millions of units).
 ---
           """)




st.markdown("### *※ A small part of the data.*")
st.dataframe(df)
# fig = go.Figure(data=[go.Table(
#     header=dict(values=list(df.columns) ,align='left'),
#     cells=dict(values=[df[col] for col in df.columns], align='left'))
# ])
# st.plotly_chart(fig)



st.sidebar.title("Sales Dashboard 📊")