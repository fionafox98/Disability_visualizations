import streamlit as st
import pandas as pd
from vega_datasets import data
import altair as alt
from altair import datum
df = pd.read_csv("~/Downloads/dataforproj.csv")

hp_mpg=alt.Chart(df).mark_bar().encode(
    y='HS:Q',
    x='Region:N',
    color='Type'
)
origins=list(df['Type'].unique())
selectOrigin=alt.selection_single(
    fields=['Type'],
    init={"Type":origins[0]},
    bind=alt.binding_select(options=origins),
    on="keyup", #disable
    clear="false"

chart = hp_mpg.encode(color="Region:N",tooltip='HS:Q').add_selection(
    selectOrigin
).transform_filter(
    selectOrigin
).properties(
    title='Percent of High School Graduates by Region with Different Types of Disabilities',
    width=200,
    height=300
)
st.altair_chart(chart, theme='streamlit')