import sounddevice as sd
import numpy as np
import soundfile as sf

def list_devices():
    print("Available audio devices:")
    devices = sd.query_devices()
    for index, device in enumerate(devices):
        print(index, device['name'], ", Core Audio (", device['max_input_channels'], "in,", device['max_output_channels'], "out)")
    print("Default input device index:", sd.default.device[1])
    print("Default output device index:", sd.default.device[1])

def record_audio(device_index, duration=10, sample_rate=44100, channels=2):
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
        print(f"Recording for {duration} seconds using device: {device_info['name']} with {channels} channels...")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, device=device_index, dtype='float32')
        sd.wait()  # Wait until recording is finished
        print("Recording done.")
        # Save recorded data as a WAV file
        output_file = 'recode/output.wav'
        sf.write(output_file, audio_data, sample_rate)
        print(f"Audio saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# List devices to find the correct one
list_devices()

# Use the correct device index from the list, e.g., 3 for Scarlett Solo
record_audio(3)
