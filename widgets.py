import streamlit as st


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

    return


if __name__ == '__main__':

    run_main()
