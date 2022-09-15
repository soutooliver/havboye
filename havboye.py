import csv
import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye prosjekt')

st.write("Innhenttest.csv")

st.file_uploader("Innhenttest.csv")

def start():
    file=open("Innhenttest.csv","a")
    file.flush()
    file.close()
    
start()
