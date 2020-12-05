import streamlit as st

#Title
st.title("Audio Book Library")
st.markdown('Divided We Stand- The Battle Over Women\'s Rights and Family Values..')
audio_file = open("divided-we-stand.mp3","rb").read()
st.audio(audio_file, format='audio/mp3')


st.markdown('Disruptive Selling: A New Strategic Approach to Sales')
audio_file = open("disruptive-selling.mp3","rb").read()
st.audio(audio_file, format='audio/mp3')


st.markdown('Emotional Habits: The 7 Things Resilient People Do Differently')
audio_file = open("emotional-habits.mp3","rb").read()
st.audio(audio_file, format='audio/mp3')
