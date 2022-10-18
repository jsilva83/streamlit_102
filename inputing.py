import streamlit as st

# Text input.
fname = st.text_input('First name', max_chars=10)
st.title(fname)

# Password.
a_pass = st.text_input('Password', type='password')

# Text area.
message = st.text_area('Message', height=200, max_chars=100)
st.write(message)

# Numbers.
a_number = st.number_input('Enter number')
b_number = st.number_input('Second number', 1, 25, 5)
c_number = st.number_input('Second number', 1.0, 25.0)

# Date and time.
a_date = st.date_input('Date?')
a_time = st.time_input('Time?')

# Color picker.
a_color = st.color_picker('Select color')
