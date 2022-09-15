import csv
import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye prosjekt')

st.write("Innhenttest.csv")

if st.button('klikk mej'):
    st.write('negro')
else:
    st.write('negro child')

def start():
    file=open("Innhenttest.csv","a")
    file.flush()
    file.close()
    
start()
