This little project is playing with Python to access the computer's microphone and save an audio file.
You can then alter the audio file, and finally send it to a 3rd party api (AssemblyAI) to change that audio to a text file.

Steps to get started:
Make sure you have a virtual environment running for python.
Run in Terminal:
    pip install matplotlib numpy
For Mac:
    brew install portaudio
    pip install pyaudio
For Windows:
    python -m pip installl pyaudio

When ready to record, Run:
python record_mic.py

Run in Terminal:
    brew install ffmpeg
    pip install pydub

On https://www.assemblyai.com get your own API Secret and add a new file api_secrets.py with that secret in the format:
API_KEY_ASSEMBLYAI = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

Just replace the X's with your key

To upload to 3rd party API to translate to text, run:
python main.py output.wav
Open output.wav.txt once completed.
Feel free to adjust the length of the audio recording and add your own audio files to translate to text. 

