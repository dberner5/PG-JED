import os
import io
import subprocess
import wave
from pydub import AudioSegment

def convert_to_wav(audio_file):
    """
    Accept a file path to an audio file and create a verson of that audio
    in .wav formate. Returns a filepath to the .wav version.
    """

    #create output file path
    output_file = list(os.path.splitext(audio_file)[:-1])
    output_file.append("_test_.wav")
    output_file = "".join(output_file)
    
    #convert audio to .wav
    subprocess.call(['ffmpeg', '-i', audio_file, output_file])
    
    #if its stereo, convert to mono
    with wave.open(output_file, 'rb') as wav_file:
        if wav_file.getnchannels() > 1:
            sound = AudioSegment.from_wav(output_file)
            sound = sound.set_channels(1)
            sound.export(output_file, format="wav")
            
    return output_file

#convert_to_wav("audio_files/Doyle Godbolt  04.26.2019.mp3")