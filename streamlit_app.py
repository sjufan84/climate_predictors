import pandas as pd
import streamlit as st
import geoviews as gv
from pathlib import Path
import holoviews as hv
from geoviews import opts

gv.extension('bokeh')

st.header('Areas of opportunity in Real Estate Based on Projected Population Migration Patterns within the US due to Climate Change')

new_combined_df = pd.read_csv(Path('./Resources/new_combined_df.csv'), index_col = [0])

new_combined_df['NAME'] = new_combined_df.index
data = gv.Dataset(new_combined_df, kdims=['Population_Delta', 'Population_Price_Discrepancy', 'NAME', '2019_home_values'])
tiles = gv.tile_sources.Wikipedia
points = data.to(gv.Points, ['LONGITUDE', 'LATITUDE'], ['Population_Delta', 'Population_Price_Discrepancy', 'NAME', '2019_home_values'])
fig = (tiles * points).opts(
    opts.Points(width=600, height=350, tools=['hover'], size=gv.dim('Population_Delta')*100,
                color='2019_home_values', cmap='reds', title = 'Counties expected to gain >= 7.5% population by 2025', show_legend=True))
analytics_df = pd.DataFrame(new_combined_df.iloc[:, -6:])

st.bokeh_chart(hv.render(fig))
st.markdown('**Size of point indicates population delta, shade of red indicates recent median home values**')
st.table(analytics_df)