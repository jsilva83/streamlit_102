# Importing standard packages.
import streamlit as st
from PIL import Image

# Applications settings.
a_icon_img = Image.open('bi.png')

# Method 1.

# With icon.
# st.set_page_config(page_title='hello',
#                    page_icon='📊'
#                    )

# With image.
# st.set_page_config(page_title='hello',  # Browser tab title.
#                    page_icon=a_icon_img,  # Icon in the browser tab.
#                    layout='wide',  # Page set to wide mode.
#                    initial_sidebar_state='collapsed',  # Controls how the sidebar shows.
#                    )

# Method 2: dictionary.
PAGE_CONFIG = {
    'page_title': 'hello',
    'page_icon': a_icon_img,
    'layout': 'centered',
    'initial_sidebar_state': 'expanded',
}
st.set_page_config(**PAGE_CONFIG)


def run_main():

    st.title('Hello Streamlit Lovers')  # Page title.
    st.sidebar.success('Menu')

    return


if __name__ == '__main__':

    run_main()
