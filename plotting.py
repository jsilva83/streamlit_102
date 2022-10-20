import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def main():

    st.title('Plotting in Streamlit')

    a_df = pd.read_csv('data/prog_languages_data.csv')
    # Display dataframe in Streamlit.
    st.dataframe(a_df)

    # Create figure; pie chart.
    a_figure = px.pie(a_df, names='lang', values='Sum', title='Programming Languages')
    st.plotly_chart(a_figure)

    # Create figure; bar chart.
    b_figure = px.bar(a_df, x='lang', y='Sum')
    st.plotly_chart(b_figure)

    return


if __name__ == '__main__':

    main()
