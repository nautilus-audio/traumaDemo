
#!/usr/bin/python
import wave
import pyaudio


from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction

#import os, glob, eyed3, ntpath, shutil

[Fs, x] = audioBasicIO.readAudioFile("OSIRIS_Motif.wav");
F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs);


chunk = 4096

f = wave.open(r"/Users/kamilahmitchell/Desktop/C++, Python & Vsts/Neurolex/OSIRIS_Motif.wav","rb")

p = pyaudio.PyAudio()
#open stream
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)
#read data
data = f.readframes(chunk)

#play stream
while data:
    stream.write(data)
    data = f.readframes(chunk)

#stop stream
stream.stop_stream()
#stream.close()

#close PyAudio
p.terminate()
