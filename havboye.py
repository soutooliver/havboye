import csv
import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye prosjekt')

csvfile = 'Innhenttest.csv'
delimiter = ','

def open_with_python_csv(Innhenttest):
    data = []
    with open(Innhenttest, 'a') as Innhenttest:
        reader = csv.reader(Innhenttest, delimiter=delimiter)

def start():
    file=open("Innhenttest.csv","a")
    file.flush()
    file.close()
    
start()
