import csv
import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye prosjekt')

# Create a section for the dataframe statistics
st.header('Statistics of Dataframe')
st.write(df.describe())
# Create a section for the dataframe header
st.header('Header of Dataframe')
st.write(df.head())
