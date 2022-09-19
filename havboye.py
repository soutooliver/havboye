import csv
import streamlit as st
import pandas as pd
import numpy as np

st.title('Havbøye prosjekt')

from iww.extractor import extractor
from iww.detector import detector
from iww.features_extraction.lists_detector import Lists_Detector as LD
from iww.features_extraction.main_content_detector import MCD

url = "http://sensor.marin.ntnu.no/logs/Gruppe11.txt"
json_file = "./iconic.json"

extractor.extract(
    url = url, 
    destination = json_file
)
