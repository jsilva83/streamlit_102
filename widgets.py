import streamlit as st
from datetime import date


def run_main():

    # Working with buttons.
    name = 'Jesse'
    if st.button('Sumbit'):

        st.write('Name: {}'.format(name.upper()))

    if st.button('Submit', key='newSubmit'):

        st.write('Name: {}'.format(name.lower()))

    # Working with radio buttons.
    status = st.radio('What is you status', ('Active', 'Inactive'))
    if status == 'Active':

        st.success('You are Active!')

    elif status == 'Inactive':

        st.warning('You are inactive!')

    # Working with Checkbox.
    if st.checkbox('Show/Hide'):

        st.text('Showing something.')

    # Working with Beta Expander.
    with st.expander('See explanation [v]', expanded=False):

        st.success('Expander text.')
        st.write("""
                The chart above shows some numbers I picked for you.\n
                I rolled actual dice for these, so they're *guaranteed* to
                be random.
            """)

    # Select / Muliple select.
    my_lang = ['', 'Python', 'c', 'Java', 'Assembly']
    choice = st.selectbox('Programming language', my_lang)
    st.write('You selected {}'.format(choice))

    # Multiple select.
    spoken_lang = ('Portuguese', 'English', 'French', 'Spanish', 'German')
    my_spoken_lang = st.multiselect('Spoken Languages', spoken_lang)
    my_other_spoken_lang = st.multiselect('Spoken Languages', spoken_lang, key='alt_lang', default='English')

    # Slider for numbers (integer, float, date.
    age = st.slider("Age", 1, 100, 50)
    my_date = st.slider('Date', date(2022, 1, 1), date(2022, 12, 31), date.today())

    # Slider for any other data type.
    color = st.select_slider("Choose color", options=['yellow', 'red', 'blue', 'black', 'white'])

    return


if __name__ == '__main__':

    run_main()
