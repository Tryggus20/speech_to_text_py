# Audio file formats: mp3, flac, wav
import wave

# Audio signal parameters:
# 1) number of channels (1 or 2 aka mono or stereo)
# 2) sample width (bits in sample)
# 3) framerate/sample_rate eg 44,100 Hz
# 4) number of frames
# 5) values of a frame


obj = wave.open("patrick.wav", "rb")

print("Number of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("parameters", obj.getparams())

# python wave_example.py 

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio) #should be framerate

frames = obj.readframes(-1)
print(type(frames), type(frames[0])) #
print(len(frames)/2) #if sample width is 2 you get double the frames

obj_new = wave.open("patrick_new.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)
obj_new.close() #duplicates the patrick file

