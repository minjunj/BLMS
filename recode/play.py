import streamlit as st
import pandas as pd
import numpy as np
from st_pages import Page, Section, show_pages, add_page_title
import time

import sounddevice as sd
import soundfile as sf


st.title('''Playing Guitar!''')

def list_devices():
    #print("Available audio devices:")
    name_dict = {}
    devices = sd.query_devices()
    i = 0
    for index, device in enumerate(devices):
        #print(index, device['name'], ", Core Audio (", device['max_input_channels'], "in,", device['max_output_channels'], "out)")
        name_dict[device['name']] = i
        i += 1
    #print(name_dict)
    return name_dict

def record_audio(device_index, duration=10, sample_rate=44100):
    """
    Records audio from the specified device for a given duration, sample rate, and number of channels.
    :param device_index: Index of the audio device to use
    :param duration: Duration in seconds of the recording
    :param sample_rate: Sampling rate of the audio in Hz
    :param channels: Number of audio channels
    :return: None, saves the audio to a file.
    """
    try:
        device_info = sd.query_devices(device_index)
        print(f"Recording for {duration} seconds using device: {device_info['name']} with {2} channels...")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, device=device_index, dtype='float32')
        sd.wait()  # Wait until recording is finished
        print("Recording done.")
        # Save recorded data as a WAV file
        output_file = 'recode/output.wav'
        sf.write(output_file, audio_data, sample_rate)
        print(f"Audio saved as {output_file}")  
    except Exception as e:
        print(f"An error occurred: {e}")
        st.error(f'An error occurred: {e}')


with st.container(border=True):
    try:
        ele = list_devices()
        input_option = st.selectbox(
        "Please Select Input Device.",
        (ele.keys()))

        output_option = st.selectbox(
        "Please Select Output Device",
        (ele.keys()))

        time_duration = st.slider("How long recode?", 0, 20, 10)
        
        if st.button("Recode"):
            with st.spinner('Wait for it...'):
                time.sleep(1)
                record_audio(ele.get(input_option), duration=10, sample_rate=44100)
    except:
        pass

st.write(f"You selected input device :{ele.get(input_option)}")
st.write(f"You selected output device :{output_option}")
st.write(time_duration, "second")


# # List devices to find the correct one
# list_devices()

# # Use the correct device index from the list, e.g., 3 for Scarlett Solo
# record_audio(3)
