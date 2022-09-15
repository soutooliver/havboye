import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye prosjekt')

def start():
    file=open("Innhenttest.csv","a")
    file.flush()
    file.close()
    
    file = 'Innhenttest.csv'
df = pd.read_csv(file,index_col=0)

print(df.head(5))
    
start()
