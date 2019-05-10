# PG-JED
This application utilizes google's speech to text API, open source NLP libraries
and some personal touches to flag if a <1min audio file contains explicit language or not

requirments:
In order to convert audio files into .WAV, you must install ffmpeg and expose that binary to windows PATH ie: C:\Users\Daniel\Downloads\ffmpeg-20190505-e384f6f-win64-static\bin

See requirements.txt for environment packages

Usage:
Pass the path to an audio file to the listen() function within main.py.  Function will return a True if profane language was detected, else False. 
