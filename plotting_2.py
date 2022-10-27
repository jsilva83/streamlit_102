import streamlit as st
import pandas as pd
import numpy as np

# Load plotting packages.
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# If a backend gui is necessary to configure. By default, this setting is not necessary.
# matplotlib.use('Agg')


def main():

    st.title('Plotting with st.pyplot.')

    a_df = pd.read_csv('data/iris.csv')  # Load csv file.

    st.dataframe(a_df.head())

    return


if __name__ == '__main__':

    main()
