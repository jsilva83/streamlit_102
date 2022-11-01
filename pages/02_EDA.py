import streamlit as st

st.subheader('EDA Page')

my_calculation = 'This is from EDA file'
st.session_state['my_calculation'] = my_calculation

st.write(my_calculation)