import streamlit as st

# Shared variables.
a_variable = st.session_state['a_variable']
my_calculation = st.session_state['my_calculation']

st.subheader('Home Page')
st.write(a_variable)
st.write(my_calculation)
