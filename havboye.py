import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye prosjekt')

def start():
    file=open("Innhenttest.csv","a")
    file.flush()
    file.close()
    
    url = 'https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv'
df = pd.read_csv(url,index_col=0)
#df = pd.read_csv(url)

print(df.head(5))
    
start()
