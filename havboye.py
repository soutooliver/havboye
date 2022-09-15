import csv
import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye prosjekt')

def start():
    file=open("Innhenttest.csv","a")
    file.flush()
    file.close()
    
start()
