import streamlit as st
from PIL import Image
import pandas as pd
import docx2txt
import pdfplumber
from PyPDF2 import PdfFileReader
import os


# Load images.
@st.cache
def load_image(a_img_file):

    a_img = Image.open(a_img_file)

    return a_img


# Usage of PyPDF2 to read pdf file (alternative to pdfplumber).
def read_pdf(a_file):

    a_pdf = PdfFileReader(a_file)
    total_page_count = a_pdf.numPages
    all_pages_text = ''

    for i in range(total_page_count):

        b_page = a_pdf.getPage(i)
        all_pages_text += b_page.extractText()

    return all_pages_text


# Function to save files.
def save_file(a_file):

    with open(os.path.join('tempdir', a_file.name), 'wb') as b_file:

        b_file.write(a_file.getbuffer())

    return st.success(f'File {a_file.name} saved to directory "tempdir"')


def main():

    st.title('File Upload Tutorial')

    a_menu = ['Image', 'Dataset', 'DocumentFiles', 'MultipleFiles', 'About']
    a_choice = st.sidebar.selectbox('Menu', a_menu)

    if a_choice == 'Image':

        st.subheader('Home')
        a_image = st.file_uploader('Upload images', type=['png', 'jpg', 'jpeg'])

        if a_image is not None:

            # st.write(type(a_image))  # Output the file type class.
            # st.write(dir(a_image))  # Output the class methods and attributes.
            a_image_details = {'filename': a_image.name, 'filetype': a_image.type, 'filesize': a_image.size}
            st.write(a_image_details)  # Outputs the dictionary with the file details.
            st.image(load_image(a_image), width=None)  # Outputs the image.

            # Save file in a directory.
            with open(os.path.join('tempdir', a_image.name), 'wb') as a_file:

                a_file.write(a_image.getbuffer())

            st.success('File saved.')

    elif a_choice == 'Dataset':

        st.subheader('Dataset')
        a_csv = st.file_uploader('Upload CSV', type=['csv'])

        if a_csv is not None:

            # st.write(type(a_csv))
            a_csv_details = {'filename': a_csv.name, 'filetype': a_csv.type, 'filesize': a_csv.size}
            st.write(a_csv_details)  # Outputs the dictionary with the file details.
            a_df = pd.read_csv(a_csv)
            st.dataframe(a_df)

    elif a_choice == 'DocumentFiles':

        st.subheader('DcoumentFiles')
        a_doc_file = st.file_uploader('Upload Document File', type=['pdf', 'docx', 'txt'])

        if st.button('Process'):

            if a_doc_file is not None:

                a_doc_details = {'filename': a_doc_file.name, 'filetype': a_doc_file.type, 'filesize': a_doc_file.size}
                st.write(a_doc_details)  # Outputs the dictionary with the file details.

                if a_doc_file.type == 'text/plain':

                    # Alternative code if the file content is to be handled as bytes.
                    # bytes_text = a_doc_file.read()  # Read as bytes.
                    # st.write(bytes_text)  # Works but in bytes.
                    # st.text(bytes_text)  # Works as expected.

                    # Read as string (decode bytes to string).
                    a_decoded_text = str(a_doc_file.read(), 'utf-8')
                    st.write(a_decoded_text)  # Wraps text and apply text styling.
                    st.text(a_decoded_text)  # Don't wrap new lines (single output line per file line).

                elif a_doc_file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':

                    a_processed_text = docx2txt.process(a_doc_file)
                    st.write(a_processed_text)
                    st.text(a_processed_text)

                elif a_doc_file.type == 'application/pdf':

                    # With pdfplumber.
                    # try:
                    #
                    #     with pdfplumber.open(a_doc_file) as a_pdf:
                    #
                    #         for page_nr in range(len(a_pdf.pages)):
                    #
                    #             st.write(f'Page nr. {page_nr}')
                    #             st.write(a_pdf.pages[page_nr].extract_text())
                    #
                    # except:
                    #
                    #     st.write('Error (PDF file processing)!')

                    # With PyPDF2
                    a_processed_text = read_pdf(a_doc_file)
                    st.write(a_processed_text)

    elif a_choice == 'MultipleFiles':

        st.subheader('Upload Multipl Files')  # Change sub-header.

        uploaded_images = st.file_uploader('Upload multiple files',
                                           type=['png', 'jpeg', 'jpg'],
                                           accept_multiple_files=True)  # get files.

        if uploaded_images is not None:

            for a_uploaded_img in uploaded_images:

                a_image_details = {'filename': a_uploaded_img.name,
                                   'filetype': a_uploaded_img.type,
                                   'filesize': a_uploaded_img.size}
                st.write(a_image_details)  # Outputs the dictionary with the file details.
                st.image(load_image(a_uploaded_img), width=None)  # Outputs the image.

    else:

        st.subheader('About')

    return


if __name__ == '__main__':

    main()
