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

# Scoring.
from rouge import Rouge


# Function using LexRank summarization algorithm.
def sumy_summarizer(docx, num=2):

    parser = PlaintextParser.from_string(docx, Tokenizer('english'))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, num)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)

    return result


# Score the result.
def score_summary(in_summary, in_reference):

    a_rouge = Rouge()
    a_score = a_rouge.get_scores(in_summary, in_reference)

    out_score_df = pd.DataFrame(a_score[0])

    return out_score_df


def main():

    st.title('Summarizer app')

    a_choice = st.sidebar.selectbox('Menu', ['Home', 'About'])

    if a_choice == 'Home':

        st.subheader('Summarization')

        a_input_text = st.text_area('Enter text here')

        if st.button('Summarize'):

            with st.expander('Original text'):

                st.write(a_input_text)

            # Layout columns to present summaries.
            left_column, right_column = st.columns(2)

            with left_column:

                with st.expander('Lex Rank Summary'):

                    a_summary = sumy_summarizer(a_input_text)
                    st.write(a_summary)

                    st.info('Score')  # Separates de output to display the score.

                    a_score_df = score_summary(a_summary, a_input_text)

                    st.dataframe(a_score_df.T)

            with right_column:

                with st.expander('TextRank Summary'):

                    st.write('gensim.summarize method is deprecated.')

    else:

        st.subheader('About')

    return


if __name__ == '__main__':

    main()
