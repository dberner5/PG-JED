import os
import pydub
import glob
from convert_audio_to_wav import convert_to_wav
from SpeechToText import SpeechToText
from profanityCheck import Profanity_Checker

"""
Call SpeechToText on an audio file to translate it to text
Call checkProfanity on the text to check for profanity
"""

audio_file = "audio_files/Doyle Godbolt  04.26.2019.mp3"
wav_file = convert_to_wav(audio_file)

# flac_files = glob.glob('audio_files/*.flac')
# flac_file = flac_files[0]

text = SpeechToText(wav_file)
# print(text)

P = Profanity_Checker()

isProfane = P.check_str(text)
# print(isProfane)

result = "{} has been analyzed:\nText: {}\nContains explicit language? {}"\
    .format(wav_file,text,isProfane)

print(result)


