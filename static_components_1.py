import streamlit as st
import streamlit.components.v1 as stc

# Local import of packages.
import a_slider


def main():

    st.title('Streamlit Static Components')  # Title of page.
    stc.html('<p style="color:red">Streamlit is Awesome</p>')  # Add html to page.
    st.markdown('<p style="color:blue">Streamlit is Awesome</p>', unsafe_allow_html=True)  # Add as markdown format.

    # Output html code.
    st.write('W3Schools Slider')
    stc.html(a_slider.a_slider)

    # Output a web site.
    stc.iframe('https://www.jcharistech.com', height=600, scrolling=True)

    return


if __name__ == '__main__':

    main()
