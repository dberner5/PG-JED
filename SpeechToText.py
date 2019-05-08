"""
Given an audio file, translate it into a string of text using Google Speech to Text API
Caveats:  The audio file needs to be mono (not sterio) and a FLAC or wav format. 
"""

import io
import os

#set credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./SpeechToText-bedba1969dba.json"

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def SpeechToText(audio_file):
    
    if os.path.splitext(audio_file)[-1] not in [".flac", ".wav", ".FLAC", ".WAV"]:
        raise ValueError("Encoding must be 'flac' or 'wav'")
    
    # Instantiates a client
    client = speech.SpeechClient()

    # Loads the audio into memory
    with io.open(audio_file, 'rb') as speech_file:
        content = speech_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        model = 'phone_call',
        language_code='en-US')
    
    # Detects speech in the audio file
    response = client.recognize(config, audio) 

    responses = []
    for result in response.results:
        responses.append(result.alternatives[0].transcript)
    return responses

#print(SpeechToText('audio_files/MAD MAC 2019-04-25.wav'))