import streamlit as st
import pandas_profiling
import pandas as pd
import os 
from streamlit_pandas_profiling import st_profile_report
from dotenv import load_dotenv

load_dotenv()

file_path = os.getenv('FILE_PATH')
file_name = os.getenv('FILE_NAME')

if os.path.exists(file_path+file_name): 
    df = pd.read_csv(file_name, index_col=None)

with st.sidebar: 
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("AutoNickML")
    choice = st.radio("Navigation", ["Upload","Profiling"])
    st.info("This project application helps you build and explore your data.")

if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

if choice == "Profiling": 
    st.title("Exploratory Data Analysis")
    profile_df = df.profile_report()
    st_profile_report(profile_df)
    st.info("This is an info")