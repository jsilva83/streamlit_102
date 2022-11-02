import streamlit as st

# EDA - Exploratory Data analysis packages
import pandas as pd

# Data vizualiation.
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# Additional packages.
# pip: gensim, sumy, gensim_sum_ext
# Not able to install the summarization library because it was deprecated
# from gensim.summarization import summarize  # TextRank algorithm.
from sumy.parsers.plaintext import PlaintextParser  # LexRank algorithm.
from sumy.nlp.tokenizers import Tokenizer  # LexRank algorithm.
from sumy.summarizers.lex_rank import LexRankSummarizer  # LexRank algorithm.


def main():

    st.title('Summarizer app')

    a_choice = st.sidebar.selectbox('Menu', ['Home', 'About'])

    if a_choice == 'Home':

        st.subheader('Summarization')

        a_input_text = st.text_area('Enter text here')

        if st.button('Summarize'):

            with st.expander('Original text'):

                st.write(a_input_text)

    else:

        st.subheader('About')

    return


if __name__ == '__main__':

    main()
