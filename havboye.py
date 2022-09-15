import csv
import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye prosjekt')

st.write("Innhenttest.csv")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

def start():
    file=open("Innhenttest.csv","a")
    file.flush()
    file.close()
    
start()
