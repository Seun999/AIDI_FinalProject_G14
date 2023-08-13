import streamlit as st
import requests
import pygame
import os

st.title("Instrument Recognition AI with Audio")
st.write("Enter the name of a musical instrument, and I'll try to recognize it!")

user_input = st.text_input("Enter an instrument name:")

if st.button("Recognize") and user_input:
    response = requests.post('http://localhost:5000/predict', json={'instrument_name': user_input})
    result = response.json()

    st.write(f"Predicted Instrument: {result['instrument_name']}")
    st.write(f"Confidence Score: {result['confidence']:.2f}")

    # Load and play the audio file corresponding to the predicted instrument
    audio_filename = f"{result['instrument_name']}.wav"
    audio_path = os.path.join(os.getcwd(), audio_filename)
    
    
    pygame.mixer.init()
    sound = pygame.mixer.Sound(audio_path)
    sound.play()
