import csv
import streamlit as st
import pandas as pd
import numpy as np
import requests

headers = []

st.title('Havbøye prosjekt')

df = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinGr4.txt", names = ['filename', 'power','location', 'time', 'lat', 'lon','Altitude','Speed','Course','Fix Mode','Reserved1','HDOP','PDOP','VDOP','Reserved2','GPS','GNSS','GLONASS','Reserved3','Teperature'])

st.header('Informasjon om bøye 4')
st.dataframe(df)

st.map(df)

