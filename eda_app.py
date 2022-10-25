# Import standard packages.
import streamlit as st
import pandas as pd


def run_eda_app():

    st.subheader('From Explaratory Data Analysis')

    a_df = pd.read_csv('data/prog_languages_data.csv')

    st.dataframe(a_df)

    return