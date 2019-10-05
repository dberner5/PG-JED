import sys
from os import listdir, remove
from os.path import isfile, isdir, join
from convert_audio_to_wav import convert_to_wav
from SpeechToText import SpeechToText
from profanityCheck import Profanity_Checker

def listen(audio_file):
    """
    This function utilizes google's speech to text API, open source NLP libraries
    and some personal touches to flag if a <1min audio file contains explicit language or not
    """

    #convert audio file to correct format
    audio_file = convert_to_wav(audio_file)

    #translate audio file into text
    text = SpeechToText(audio_file)

    #check text for profanity
    P = Profanity_Checker()
    isProfane = P.check_list(text)

    #clean up audio file by removing _test_.wav copy used in the api
    remove(audio_file)

    print("#################################################\n")

    print(f"{audio_file} has been analyzed:")
    return (text, isProfane)

def listenAll(directory):
    print("called listenAll")
    audio_files = [f for f in listdir(directory) if isfile(join(directory, f))]
    return [listen(join(directory, audio_file)) for audio_file in audio_files]

if __name__ == "__main__":
    assert len(sys.argv) == 2
    if isfile(sys.argv[1]):
        print(listen(sys.argv[1]))
    if isdir(sys.argv[1]):
        print(listenAll(sys.argv[1]))
