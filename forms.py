# Import standard packages.
import streamlit as st
import pandas as pd


def main():

    st.title('Calculator and Forms')  # Page title.
    a_choice = st.sidebar.selectbox('Menu', ['Calculator', 'About'])  # Page menu.

    if a_choice == 'Calculator':

        st.subheader('Forms tutorial')

        # Method 1: Context Manager approach (using with).
        with st.form(key='form1'):

            firstname = st.text_input('First Name')
            lastname = st.text_input('Last Name')
            date_of_birth = st.date_input('Date of Birth')
            submitt_btn = st.form_submit_button(label='SignUp')

        if submitt_btn:  # This can be done inside or outside of the "with" clause.

            st.success(f'Hi {firstname} {lastname}, you have created an account.')

        # Method 2: using a declared form object.
        form2 = st.form(key='form2')
        username = form2.text_input('Username')
        jobtype = form2.selectbox('Job', ['Developer', 'Data Scientist', 'Database Administrator'])
        submitt_btn_2 = form2.form_submit_button(label='Login')

        if submitt_btn_2:

            st.success(f'{username} successfuly loged in.')

        # Form in columns: Salary calculator.
        with st.form(key='salary_form'):

            column_1, column_2, column_3 = st.columns(3)

            with column_1:

                hourly_rate = st.number_input('Hourly rate in $USD', 50.0)

            with column_2:

                nr_hours_per_week = st.number_input('Hours per week', 1, 60, 40)

            with column_3:
                st.text('Salary')
                submit_salary_btn = st.form_submit_button(label='Salary')

        if submit_salary_btn:

            with st.expander('Results'):

                daily_salary = [hourly_rate * 8]
                weekly_salary = [hourly_rate * nr_hours_per_week]

                a_df = pd.DataFrame({'hourly_rate': [hourly_rate],
                                     'daily_salary': daily_salary,
                                     'weekly_salary': weekly_salary})
                # st.dataframe(a_df)  # One line with 3 columns.
                st.dataframe(a_df.T)  # Transpose the matrix.

    else:

        st.subheader('Forms and calculator application.')

    return


if __name__ == '__main__':

    main()
