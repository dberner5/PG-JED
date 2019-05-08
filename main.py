from convert_audio_to_wav import convert_to_wav
from SpeechToText import SpeechToText
from profanityCheck import Profanity_Checker

"""
This application utilizes google's speech to text API, open source NLP libraries
and some personal touches to flag if a <1min audio file contains explicit language or not
"""

def listen(audio_file):

    #convert audio file to correct format
    audio_file = convert_to_wav(audio_file)

    #translate audio file into text
    text = SpeechToText(audio_file)

    #check text for profanity
    P = Profanity_Checker()
    isProfane = P.check_str(text)

    result = f"{audio_file} has been analyzed:\nText: {text}\nContains explicit language? {isProfane}"
    print(result)
    return isProfane

#listen("audio_files/JED Golf 05.03.2019.mp3")

