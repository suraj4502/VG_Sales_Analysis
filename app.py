import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title="VG Sales Dashboard.",page_icon="🎮",
    layout="wide",menu_items={
        'About': 'A Dashboard for Video Game Sales Analysis.'
    })






    


df = pd.read_csv('vgsales.csv')
df['Publisher'].fillna('Unknown',inplace=True)
sales = ['NA_Sales','EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
df[sales] = df[sales] * 1000000


st.sidebar.image('giphy.gif',width=150) #use_column_width=True,
st.sidebar.title("Sales Dashboard 📊")
st.sidebar.markdown("---")


rd =st.sidebar.radio('Select Analysis🎮',['Overview.',
                                        'Year wise Analyis.',
                                        'Genre wise Analysis.',
                                        'Platform wise Analysis.',
                                        'Publisher wise Analysis.'
                                        ])



# OVERWIEW

if rd == 'Overview.':
    st.title('Video Games Sales Analysis...🎮')


    st.markdown("---")
    ts = df['Global_Sales'].sum()/1000000
    tg = df.shape[0]
    tp = len(df['Publisher'].unique())
    
    col1, col2, col3 = st.columns(3) 
    col1.metric(label="Total Sales.", value=str(ts)+ ' M',delta="+")
    col2.metric(label="Total Games Released.", value=tg ,delta="+", )
    col3.metric(label='Total Pulishers.',value=tp, delta="+")
    st.markdown("---")
    
    
    image = Image.open('sales.png')
    st.image(image)
    
    
    
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





# YEAR WISE ANALYSIS
if rd == 'Year wise Analyis.':
    

    st.title("Year Wise Analysis📅")
    st.markdown("---")
    
    st.header("Total Global Sales Over Time.")
    fig = px.line(df.groupby('Year')['Global_Sales'].sum().reset_index(), x='Year', y='Global_Sales')
    fig.update_yaxes(title_text='Global Sales')
    fig.update_traces(line=dict(color='red'))
    fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Sales',
    width=800,
    height=400,
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='#61677A'),
    hovermode='x',  # Show tooltips on hover
    hoverlabel=dict(bgcolor='#1A1A40', font_size=12),  # Tooltip style
    )
    fig.update_layout(plot_bgcolor='#0E1117' ,)
    st.plotly_chart(fig)
    
    st.header('Sales by Region Over Time.')
    
    region_sales_over_time = df.groupby('Year')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum().reset_index()
    fig = px.line(region_sales_over_time, x='Year', y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'],
                  color_discrete_sequence=['#00DFA2', '#D80032', '#F78CA2', '#3DB2FF'])
    
    fig.update_traces(
    name='North America',
    selector=dict(name='NA_Sales')
    )

    fig.update_traces(
        name='Europe',
        selector=dict(name='EU_Sales')
    )

    fig.update_traces(
        name='Japan',
        selector=dict(name='JP_Sales')
    )

    fig.update_traces(
        name='Other',
        selector=dict(name='Other_Sales')
    )
    fig.update_layout(
    plot_bgcolor='#0E1117' ,
    width=800,
    height=400,
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='#61677A'),
    hoverlabel=dict(bgcolor='#1A1A40', font_size=12),  # Tooltip style
    )
    st.plotly_chart(fig)
    
    
    st.header("Number of Games Released Over Time.")
    games_released_over_time = (df.groupby('Year')['Name'].count().reset_index()).rename(columns = {'Name':'count'})
    fig = px.bar(games_released_over_time, x='Year', y='count',text_auto=True,
             color_discrete_sequence=['#FCAEAE'])
    
    fig.update_xaxes(title_text='Year', tickmode='linear', tick0=2010, dtick=1)
    fig.update_yaxes(title_text='Count')
    fig.update_layout(
    plot_bgcolor='#0E1117' ,
    width=800,
    height=400,
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='#61677A'),
    hoverlabel=dict(bgcolor='#1A1A40', font_size=12),  # Tooltip style
    )
   
    st.plotly_chart(fig)
    
    st.header('Average Sales Per Game Over Time.')
    # Average Sales Per Game Over Time (Line Chart)
    average_sales_over_time = df.groupby('Year')['Global_Sales'].mean().reset_index()
    fig = px.line(average_sales_over_time, x='Year', y='Global_Sales')
    fig.update_yaxes(title_text='Avg Global Sales')
    fig.update_traces(line=dict(color='red'))
    fig.update_layout(
    plot_bgcolor='#0E1117' ,
    width=800,
    height=400,
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='#61677A', linewidth=0.3),
    hoverlabel=dict(bgcolor='#1A1A40', font_size=12),  # Tooltip style
    )
    st.plotly_chart(fig)
    
    
    
    
    
## GENRE WISE ANALYSIS:


if rd == 'Genre wise Analysis.':
    st.title("Genre Wise Analysis⚔️")
    
    st.markdown("---")
    
    
    st.header("Genre Popularity.")
    genre_popularity = df['Genre'].value_counts().reset_index()
    genre_popularity.columns = ['Genre', 'Count']
    fig = px.bar(genre_popularity, x='Genre', y='Count',color_discrete_sequence=['#00DFA2'] )
    fig.update_layout(
    xaxis_title='Genre',
    yaxis_title='Count',
    width=800,
    height=400,
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='lightgray'),
    legend_title_text='Genres',
    hovermode='x',  # Show tooltips on hover
    hoverlabel=dict(bgcolor='#3F2305', font_size=12),  # Tooltip style
    )
    fig.update_layout(plot_bgcolor='#0E1117' ,)
    st.plotly_chart(fig)
    
    
    st.header("Total Sales by Genre.")
    # Total Sales by Genre (Bar Chart)
    total_sales_by_genre = df.groupby('Genre')['Global_Sales'].sum().reset_index()
    fig = px.bar(total_sales_by_genre, x='Genre', y='Global_Sales',color_discrete_sequence=['#E23E57'])
    fig.update_layout(
    xaxis_title='Genre',
    yaxis_title='Sales',
    width=800,
    height=400,
    margin=dict(l=50, r=50, t=50, b=20),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='lightgray'),
    legend_title_text='Genres',
    hovermode='x',  # Show tooltips on hover
    hoverlabel=dict(bgcolor='#3F2305', font_size=12),  # Tooltip style
    )
    fig.update_layout(plot_bgcolor='#0E1117' ,)
    st.plotly_chart(fig)
    
    
    st.header("Market Share by Genre.")
    # Market Share by Genre (Pie Chart)
    market_share_by_genre = df.groupby('Genre')['Global_Sales'].sum().reset_index()
    fig = px.pie(market_share_by_genre, values='Global_Sales', names='Genre',
             color_discrete_sequence=px.colors.sequential.Rainbow_r)
    
    fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    legend_title_text='Genres',
    hovermode='x',  # Show tooltips on hover
    hoverlabel=dict(bgcolor='#311D3F', font_size=12),  # Tooltip style
    )
    fig.update_layout(plot_bgcolor='#0E1117' ,)
    st.plotly_chart(fig)
    
    
    st.header("Top Games in Each Genre.")
    top_games_by_genre = df.groupby('Genre').apply(lambda x: x.nlargest(1, 'Global_Sales')).reset_index(drop=True)
    
    st.dataframe(top_games_by_genre)
    

if rd == 'Platform wise Analysis.':
    st.title("Platform Wise Analysis🧿")
    
    st.markdown("---")
    
    # Platform Popularity (Bar Chart)
    st.header('Platform Popularity.')
    platform_popularity = df['Platform'].value_counts().reset_index()
    platform_popularity.columns = ['Platform', 'Count']
    fig = px.bar(platform_popularity, x='Platform', y='Count',color_discrete_sequence= ['#6528F7'])
    fig.update_layout(
    xaxis_title='Platform',
    yaxis_title='Count',
    width=800,
    height=400,
   
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='#F2DEBA'),
    legend_title_text='Genres',
    hovermode='x',  # Show tooltips on hover
    hoverlabel=dict(bgcolor='#3F2305', font_size=18),  # Tooltip style
    )
    fig.update_layout(plot_bgcolor='#0E1117' ,)
    st.plotly_chart(fig)
    
    
    #'Market Share by Platform'
    st.header('Market Share by Platform.')
    market_share_by_platform = df.groupby('Platform')['Global_Sales'].sum().reset_index()
    fig = px.pie(market_share_by_platform, values='Global_Sales', names='Platform')
    custom_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    fig.update_traces(marker=dict(colors=custom_colors))
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
                showlegend=False,# Hide the legends
                width=800,
    height=400,
                )
    fig.update_layout(plot_bgcolor='#0E1117' ,)
    st.plotly_chart(fig)
    
    
    
    
    
    
    
    # Total Sales by Platform (Bar Chart)
    st.header('Total Sales by Platform.')
    total_sales_by_platform = df.groupby('Platform')['Global_Sales'].sum().reset_index().sort_values('Global_Sales', ascending=False)
    fig = px.bar(total_sales_by_platform, x='Platform', y='Global_Sales',
                color_discrete_sequence=['#3CCF4E'])
    
    fig.update_layout(width=800,
    height=400,)
    fig.update_layout(plot_bgcolor='#0E1117' ,)
    st.plotly_chart(fig)
    
    
    
    # Platform Sales by Region (Stacked Bar Chart)
    st.header("Platform Sales by Region.")
    
    region_sales_by_platform = df.groupby('Platform')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum().reset_index()
    fig = px.bar(region_sales_by_platform, x='Platform', y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'],
              barmode='stack')
    
    fig.update_layout(
    xaxis_title='Platform',
    yaxis_title='Sales',
    width=800,
    height=400,
    margin=dict(l=10, r=10, t=10, b=10),)
    fig.update_layout(plot_bgcolor='#0E1117' ,)
    fig.update_traces(
    name='North America',
    selector=dict(name='NA_Sales')
    )

    fig.update_traces(
        name='Europe',
        selector=dict(name='EU_Sales')
    )

    fig.update_traces(
        name='Japan',
        selector=dict(name='JP_Sales')
    )

    fig.update_traces(
        name='Other',
        selector=dict(name='Other_Sales')
    )
    
    st.plotly_chart(fig)
    
    st.header("Top Games on Each Platform.")
    # Top Games on Each Platform (Table)
    top_games_by_platform = df.groupby('Platform').apply(lambda x: x.nlargest(1, 'Global_Sales')).reset_index(drop=True)
    st.dataframe(top_games_by_platform)
    
    
    
if rd == 'Publisher wise Analysis.':
    st.title("Publisher Wise Analysis🕹️")
    
    st.markdown("---")
    
    # Top Publishers by Sales (Bar Chart)
    st.header('Top Publishers by Sales')
    top_publishers_by_sales = df.groupby('Publisher')['Global_Sales'].sum().reset_index()
    top_publishers_by_sales = top_publishers_by_sales.sort_values(by='Global_Sales', ascending=False).head(10)
    fig = px.bar(top_publishers_by_sales, x='Publisher', y='Global_Sales',
                 color_discrete_sequence=['#45FFCA'])
    
    fig.update_layout(
    xaxis_title='Publisher',
    yaxis_title='Sales',
    width=800,
    height=400,
    margin=dict(l=10, r=10, t=10, b=10),)
    fig.update_layout(plot_bgcolor='#0E1117' ,)
    st.plotly_chart(fig)
    
    
    st.header('publisher Market Share.')
    # Publisher Market Share (Pie Chart)
    publisher_market_share = df.groupby('Publisher')['Global_Sales'].sum().reset_index()
    publisher_market_share = publisher_market_share.sort_values(by='Global_Sales', ascending=False).head(10)
    fig = px.pie(publisher_market_share, values='Global_Sales', names='Publisher',
                 color_discrete_sequence=px.colors.sequential.Jet_r)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
    xaxis_title='Publisher',
    yaxis_title='Sales',
    width=800,
    height=400,
    margin=dict(l=10, r=10, t=10, b=10),
    showlegend = False) 
    fig.update_layout(plot_bgcolor='#0E1117' ,)   
    st.plotly_chart(fig)
    
    
    st.header('Publishers Top Games.')
    # Publisher's Top Games (Table)
    top_games_by_publisher = df.groupby('Publisher').apply(lambda x: x.nlargest(1, 'Global_Sales')).reset_index(drop=True)
    st.dataframe(top_games_by_publisher)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
st.sidebar.markdown("---")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")
st.sidebar.markdown("\n")







#st.markdown("---")
st.sidebar.markdown("- Developed by `SKY`.   ⇨[github ](https://github.com/suraj4502), [Linkedin](https://www.linkedin.com/in/suraj4502), [Ig](https://www.instagram.com/suraj452/).")
#st.markdown("---")