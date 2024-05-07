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
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, device=device_index, dtype='float32')
        sd.wait()  # Wait until recording is finished
        # Save recorded data as a WAV file
        output_file = 'recoded/output.wav'
        sf.write(output_file, audio_data, sample_rate)
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
        col1, col2 = st.columns([0.2, 1.4])
        with col1:
            if st.button("Recode"):
                st.session_state["Recode"] = True
        with col2:
            if st.button("Save"):
                st.session_state["Save"] = True
        if 'Recode' in st.session_state and st.session_state['Recode']:
            with st.spinner('recording...'):
                time.sleep(1)
                record_audio(ele.get(input_option), duration=time_duration, sample_rate=44100)
                st.audio("recoded/output.wav", format="audio/mpeg", loop=False)
                st.session_state['Recode'] = False
        if 'Save' in st.session_state and st.session_state['Save']:
            st.write("Shot Auto Chord")
            st.success('This is a success message!')
            st.session_state['Save'] = False
    except:
        pass

# st.write(f"You selected input device :{ele.get(input_option)}")
# st.write(f"You selected output device :{output_option}")
# st.write(time_duration, "second")
