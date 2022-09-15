import csv
import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye prosjekt')

df = pd.read_csv("dir/Innhenttest.csv")

@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')


csv = convert_df(df)

st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)

def start():
    file=open("Innhenttest.csv","a")
    file.flush()
    file.close()
    
start()
