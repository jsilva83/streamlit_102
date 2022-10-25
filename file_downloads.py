# Import standard packages.
import streamlit as st
import streamlit.components as stc


def main():

    st.title('File downloads App')

    a_menu = ['Home', 'CSV', 'About']
    a_choice = st.sidebar.selectbox('Menu', a_menu)

    if a_choice == 'Home':

        st.subheader('Home')  # Page title.

        a_text = st.text_area('Your message')  # Input a message.

        if st.button('Save'):  # If the button is pressed, execute the code block.

            st.write(a_text)  # Output the inputed message.

    elif a_choice == 'CSV':

        st.subheader('CSV')

    else:

        st.subheader('About')

    return


if __name__ == '__main__':

    main()
