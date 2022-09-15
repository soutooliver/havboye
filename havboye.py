import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye prosjekt 2022')

def start():
    file=open("Innhenttest.csv","a")
    file.write(str(response)+",")
    file.flush()
    file.close()
    
start()
