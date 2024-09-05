import streamlit as st
import numpy as np 
import pandas as pd 
import plotly.express as px 

st.set_page_config(layout='wide')

df = pd.read_csv('india.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India Data Vizualization')

selected_states = st.sidebar.selectbox('Select a State',list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('size represents primary parameter')
    st.text('color represents secondary parameter')
    if selected_states=='Overall India':
      

        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",size=primary,color=secondary,zoom=4, mapbox_style="carto-positron",size_max=35,width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = df[df['State']==selected_states]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude",size=primary,color=secondary,zoom=4, mapbox_style="carto-positron",size_max=35,width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
        
