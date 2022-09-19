import csv
import streamlit as st
import pandas as pd
import numpy as np

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
   st.header('Dope brah')
   st.write(df.head())
   # Create a section for matplotlib figure
   st.header('Plot of Data')
   fig, ax = plt.subplots(1,1)
   ax.scatter(x=df['Depth'], y=df['Magnitude'])
   ax.set_xlabel('Depth')
   ax.set_ylabel('Magnitude')
   st.pyplot(fig)
