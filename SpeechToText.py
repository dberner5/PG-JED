"""
Given an audio file, translate it into a string of text using Google Speech to Text API
"""

import io
import os

#set credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./SpeechToText-bedba1969dba.json"

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = "RecordingMono.flac"

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=44100,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio) #crashing here

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
    print("hello speech to text")