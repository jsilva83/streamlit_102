import streamlit as st


def main():

    st.title('File Upload Tutorial')

    a_menu = ['Image', 'Dataset', 'DocumentFiles', 'About']
    a_choice = st.sidebar.selectbox('Menu', a_menu)

    if a_choice == 'Image':

        st.subheader('Home')
        a_image = st.file_uploader('Upload images', type=['png', 'jpg', 'jpeg'])

        if a_image is not None:

            st.write(type(a_image))

    elif a_choice == 'Dataset':

        st.subheader('Dataset')

    elif a_choice == 'DocumentFiles':

        st.subheader('DcoumentFiles')

    else:

        st.subheader('About')

    return


if __name__ == '__main__':

    main()
