# External packages.
import streamlit as st
import pandas as pd


# Main function.
def run_main():

    # Formating text.
    st.title('This is a title - Hello world')
    st.text("This is a piece of text.")
    name = 'Jesse'
    st.text("This is cool - another piece of text with var {}.".format(name))
    st.header("This is a header")
    st.subheader('This is  subheader')
    st.markdown('## This is markdown!')

    # Displaying colored text.
    st.success('Successful.')
    st.warning('This is dangerous.')
    st.info('Pay attention to this.')
    st.error('This is an error.')
    st.exception('This is an exception.')

    # Superfunction write.
    st.write('### This is a "write" text.')
    st.write(1+2)

    # Get help.
    st.help(range)  # Help on python function range.
    st.write(dir(st))   # All 'st' commands!

    # Display data.
    df = pd.read_csv('iris.csv')

    # Method 1.
    st.text('Display dataframe.')
    st.dataframe(df)
    # With size.
    st.text('Display dataframe and add sizing.')
    st.dataframe(df, 600, 600)
    # With color.
    st.text('Display dataframe and add color to maximum values in columns.')
    st.dataframe(df.style.highlight_max(axis=0))
    # st.text('Display dataframe and add color to maximum values in rows.') # Does not work.
    # st.dataframe(df.style.highlight_max(axis=1))  # Does not work.

    # Method 2.
    st.text('Display dataframe as a static table.')
    st.table(df)

    # Method 3.
    st.text('Display dataframe with "write" function.')
    st.write(df)

    # Method 4.
    st.text('Displaying JSON formated data.')
    st.json({'data': 'name', 'age': 45, 'year_of_birdth': 1965})

    # Render code.
    st.text('Rendering code.')
    mycode = """
    def sayhello():
        print('Hello world")
    """
    st.code(mycode, language='python')

    return


if __name__ == '__main__':
    run_main()
