from pydub import AudioSegment

audio = AudioSegment.from_wav("output.wav")

#this increases volume by 6dB
audio = audio + 6

audio = audio * 2 #loops it once through

audio = audio.fade_in(2000) #miliseconds

audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")
print("done")
