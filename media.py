import streamlit as st
from PIL import Image

# Working with media files.
img = Image.open('data/image_03.jpg')
# st.image(img) # simple alternative.
st.image(img, use_column_width=True)    # takes all the column space.

# Image from a URL.
st.image('https://images.unsplash.com/photo-1664783463257-039020b8acac?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1506&q=80')

# working with videos.
video_file = open('data/secret_of_success.mp4', 'rb').read()
st.video(video_file)
# st.video(video_file, start_time=3)

# Play audio.
audio_file = open('data/song.mp3', 'rb')
st.audio(audio_file)
# st.audio(audio_file.read(), format='audio/mp3')
