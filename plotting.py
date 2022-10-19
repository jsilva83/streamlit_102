import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def main():

    st.title('Plotting in Streamlit')

    a_df = pd.read_csv('data/prog_languages_data.csv')
    # Display dataframe in Streamlit.
    st.dataframe(a_df)

    return


if __name__ == '__main__':

    main()
