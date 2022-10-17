import streamlit as st

# Text input.
fname = st.text_input('First name', max_chars=10)
st.title(fname)

# Text area.
message = st.text_area('Message', height=200, max_chars=100)
st.write(message)

# Numbers.
a_number = st.number_input('Enter number')
b_number = st.number_input('Second number', 1, 25)
