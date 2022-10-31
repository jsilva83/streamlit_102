import streamlit as st
import streamlit.components.v1 as stc


def main():

    st.title('Streamlit Static Components')  # Title of page.
    stc.html('<p style="color:red">Streamlit is Awesome</p>')  # Add html to page.
    st.markdown('<p style="color:blue">Streamlit is Awesome</p>', unsafe_allow_html=True)  # Add as markdown format.

    return


if __name__ == '__main__':

    main()
