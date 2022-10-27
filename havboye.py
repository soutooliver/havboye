import csv
import streamlit as st
import pandas as pd
import numpy as np
import requests

headers = []

st.title('Havbøye prosjekt')

df1 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB1.txt", names = ['filename', 'power','location', 'time', 'lat', 'lon','Altitude','Speed','Course','Fix Mode','Reserved1','HDOP','PDOP','VDOP','Reserved2','GPS','GNSS','GLONASS','Reserved3','Teperature'])
df2 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB2.txt", names = ['filename', 'power','location', 'time', 'lat', 'lon','Altitude','Speed','Course','Fix Mode','Reserved1','HDOP','PDOP','VDOP','Reserved2','GPS','GNSS','GLONASS','Reserved3','Teperature'])
df3 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB3.txt", names = ['filename', 'power','location', 'time', 'lat', 'lon','Altitude','Speed','Course','Fix Mode','Reserved1','HDOP','PDOP','VDOP','Reserved2','GPS','GNSS','GLONASS','Reserved3','Teperature'])
df4 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB4.txt", names = ['filename', 'power','location', 'time', 'lat', 'lon','Altitude','Speed','Course','Fix Mode','Reserved1','HDOP','PDOP','VDOP','Reserved2','GPS','GNSS','GLONASS','Reserved3','Teperature'])
df5 = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinB5.txt", names = ['filename', 'power','location', 'time', 'lat', 'lon','Altitude','Speed','Course','Fix Mode','Reserved1','HDOP','PDOP','VDOP','Reserved2','GPS','GNSS','GLONASS','Reserved3','Teperature'])

st.header('Informasjon om bøye 1')
st.dataframe(df1)
col1.metric("Temperature", "70 °C", "1.2 °C")
st.map(df1)

st.header('Informasjon om bøye 2')
st.dataframe(df2)
st.map(df2)

st.header('Informasjon om bøye 3')
st.dataframe(df3)
st.map(df3)

st.header('Informasjon om bøye 4')
st.dataframe(df4)
st.map(df4)

st.header('Informasjon om bøye 5')
st.dataframe(df5)
st.map(df5)
