
#!/usr/bin/python


from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt


#Import & Analyze Audio Signal
[Fs, x] = audioBasicIO.readAudioFile("OSIRIS_Motif.wav");

#Mono
if (x.any()==1):
    nuX = audioBasicIO.stereo2mono(x);
    F = audioFeatureExtraction.stFeatureExtraction(nuX, Fs, 0.050*Fs, 0.025*Fs);

#Stereo
else:
    F = audioFeatureExtraction.stFeatureExtraction(x[:,0], Fs, 0.050*Fs, 0.025*Fs)


plt.subplot(2,1,1); plt.plot(F[0,:]); plt.xlabel('Frame no'); plt.ylabel('ZCR');
plt.subplot(2,1,2); plt.plot(F[1,:]); plt.xlabel('Frame no'); plt.ylabel('Energy');
plt.subplot(2,1,9); plt.plot(F[9,:]); plt.xlabel('Frame no'); plt.ylabel('MFCC'); plt.show()






#Citations
'''
@article{giannakopoulos2015pyaudioanalysis,
    title={pyAudioAnalysis: An Open-Source Python Library for Audio Signal Analysis},
        author={Giannakopoulos, Theodoros},
            journal={PloS one},
                volume={10},
                    number={12},
                        year={2015},
                            publisher={Public Library of Science}
}
'''
