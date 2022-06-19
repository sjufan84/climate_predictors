import pandas as pd
import streamlit as st
from pathlib import Path
import os
from dotenv import load_dotenv
from pathlib import Path


import plotly.express as px

load_dotenv()
mapbox_access_token = os.getenv('MAPBOX_ACCESS_TOKEN')


st.markdown('#### *Map is interactive.*  **Size of point indicates population delta, shade of red indicates recent median home values.**')

new_combined_df = pd.read_csv(Path('./Resources/new_combined_df.csv'), index_col = [0])

fig = px.scatter_mapbox(new_combined_df, lat="LATITUDE", lon="LONGITUDE", color="2019_home_values", size = 'Population_Delta_Raw', labels = {'2019_home_values' : 'Median Home Values'},
                        color_continuous_scale='reds', zoom=2.25, mapbox_style="open-street-map", center = {'lon': -97, 'lat' : 37.11}, height = 500, width = 750, 
                        hover_data = ['NAME.1', '2019_home_values', 'Population_Delta', 'Population_Delta_Raw'], title = '2025 Migration Projections and Home Value Data by County')


st.plotly_chart(fig)


analytics_df = pd.DataFrame(new_combined_df.iloc[:, -6:])

st.markdown('#### Table below contains data for all counties in the US projected to increase in size by 7.5% or more by 2025 (table can be expanded)')
st.table(analytics_df)