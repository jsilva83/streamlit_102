# Import standard packages.
import streamlit as st
import logging  # enables logging

# Import my packages.
from eda_app import run_eda_app
from ml_app import run_ml_app

# Constants.
LOGS_FORMAT = '%(levelname)s %(asctime)s.%(msecs)03d - %(message)s'

# Create a logger to a teminal.
logging.basicConfig(level=logging.DEBUG, format=LOGS_FORMAT)
a_logger = logging.getLogger(__name__)

# Create a logger to a file.
b_logger = logging.getLogger(__name__)  # Create logger process.
b_logger.setLevel(logging.DEBUG)  # Set logger logging level.
b_formatter = logging.Formatter(LOGS_FORMAT)  # Define format of logs.
b_file_handler = logging.FileHandler('activity.log')  # Set a file handler.
b_file_handler.setFormatter(b_formatter)  # Set the formatting of messages.
b_logger.addHandler(b_file_handler)  # Set the file to send logging activity.


def main():

    st.title('Main App')

    a_menu = ['Home', 'EDA', 'ML', 'About']
    a_choice = st.sidebar.selectbox('Menu', a_menu)

    if a_choice == 'Home':

        b_logger.info('Home section')  # Log home section.

        st.subheader('Home')

    elif a_choice == 'EDA':

        b_logger.info('EDA section')  # Log EDA section.

        st.subheader('EDA')
        run_eda_app()

    elif a_choice == 'ML':

        b_logger.info('ML section')  # Log ML section.

        st.subheader('ML')
        run_ml_app()

    else:

        b_logger.info('About section')  # Log about section.

        st.subheader('About')

    return


if __name__ == '__main__':

    main()
