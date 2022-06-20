import wave

# Open the file in read-binary format
obj = wave.open("patrick.wav", "rb")

print(f""" Number of channels: {obj.getnchannels()}
Sample width: {obj.getsampwidth()}
Frame rate: {obj.getframerate()}
Number of frames: {obj.getnframes()}
All Parameters: {obj.getparams()}
""")

# Calculate time of audio in secs
t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

# get the actual frames 
frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames) / 2)  # 2 is the sample width

obj.close()


# Writing and Saving the data
obj_new = wave.open("patrick_new.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)

obj_new.close()