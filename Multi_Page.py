import streamlit as st


def main():

    # Share variables.
    a_variable = 'Variable "a_variable" from "multi-page.py".'
    st.session_state['a_variable'] = a_variable

    if 'my_calculation' not in st.session_state:
        st.session_state['my_calculation'] = ''

    st.title('Streamlit multi-page application')
    st.subheader('Main page')
    st.write(a_variable)

    a_calculation = st.session_state['my_calculation']
    st.write(f'my_calculation: {a_calculation}')

    a_choice = st.sidebar.selectbox('Submenu', ['Pandas', 'Tensorflow'])
    if a_choice == 'Pandas':

        st.subheader('Pandas')

    else:

        st.subheader('Tensorflow')

    return


if __name__ == '__main__':

    main()
