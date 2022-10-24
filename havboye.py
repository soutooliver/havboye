import csv
import streamlit as st
import pandas as pd
import numpy as np
import requests

headers = []

st.title('Havbøye prosjekt')

df = pd.read_csv("http://sensor.marin.ntnu.no/logs/UlsteinGr4.txt", names = ['filename', 'power','location', 'time', 'lat', 'lon','Altitude','Speed','Course','Fix Mode','Reserved1','HDOP','PDOP','VDOP','Reserved2','GPS','GNSS','GLONASS','Reserved3'])

st.header('Informasjon om bøye 4')
st.dataframe(df)

st.pydeck_chart(pydeck_obj=df, use_container_width=False)

st.text("Test")

'''
url = 'http://sensor.marin.ntnu.no/logs/UlsteinGr4.txt'
request = requests.get(url)
print(request.text)

st.title('Havbøye prosjekt')

# Add a title and intro text
st.text('Denne nettsida viser til informasjon om havbøya')
# Create file uploader object
upload_file = st.file_uploader('Last opp fil med informasjon om havbøya')
# Check to see if a file has been uploaded
if upload_file is not None:
   # If it has then do the following:
   # Read the file to a dataframe using pandas
   df = pd.read_csv(upload_file)
   # Create a section for the dataframe statistics
   st.header('Statistikk om havbøya')
   st.write(df.describe())
   # Create a section for the dataframe header
   st.header('Informasjon')
   st.write(df.head())

   df = pd.DataFrame(
    np.random.randn(1, 2) / [50, 50] + [62.3433, 5.8488],
    columns=['lat', 'lon'])
'''
