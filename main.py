import os
from convert_audio_to_wav import convert_to_wav
from SpeechToText import SpeechToText
from profanityCheck import Profanity_Checker

def listen(audio_file):
    """
    This application utilizes google's speech to text API, open source NLP libraries
    and some personal touches to flag if a <1min audio file contains explicit language or not
    """

    #convert audio file to correct format
    audio_file = convert_to_wav(audio_file)

    #translate audio file into text
    text = SpeechToText(audio_file)

    #check text for profanity
    P = Profanity_Checker()
    isProfane = P.check_str(text)

    #format readable result string
    result = f"{audio_file} has been analyzed:\nText: {text}\nContains explicit language? {isProfane}"
    print(result)

    #clean up audio file by removing _test_.wav copy used in the api
    os.remove(audio_file)

    return isProfane

listen("audio_files/29-089531s.wav")

