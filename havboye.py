import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye prosjekt 2022')

def start():
    response=send_at_get_resp("AT+CGNSINF")
    print("Ulstein TOF2 Bøye nr1 "+response)
    file=open("Innhenttest.csv","a")
    file.write(str(response)+",")
    file.flush()
    file.close()
    
start()
