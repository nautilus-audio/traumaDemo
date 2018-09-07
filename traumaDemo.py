
#!/usr/bin/python
'''
Use Feature Extraction from pyAudioAnalyis to analyze voice samples with MFCC. Calculate to get fundamental frequency. Calculate formant from F0. Then calculate first formant using the average vocal human tract length, and subsequent formants.
'''


from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt
import matplotlib.pyplot as style


#Import & Analyze Audio Signal
nfft = 64
X = 64
nceps = 32

[Fs, x] = audioBasicIO.readAudioFile("PTSD_female.wav");


#Mono
if (x.any==1):
    nuX = audioBasicIO.stereo2mono(x);
    F = audioFeatureExtraction.stFeatureExtraction(nuX, Fs, 0.050*Fs, 0.025*Fs);
#Stereo
else:
    F = audioFeatureExtraction.stFeatureExtraction(x[:,0], Fs, 0.050*Fs, 0.025*Fs)


[fbank, freqs] = audioFeatureExtraction.mfccInitFilterBanks(Fs, nfft)


ceps = audioFeatureExtraction.stMFCC(X, fbank, nceps);

print ceps

#chn = audiofile.channels

'''
#Mono
if (x.any==1):
    nuX = audioBasicIO.stereo2mono(x);
    F = audioFeatureExtraction.stFeatureExtraction(nuX, Fs, 0.050*Fs, 0.025*Fs);
#Stereo
elif (x.any==2):
    F = audioFeatureExtraction.stFeatureExtraction(x[:,0], Fs, 0.050*Fs, 0.025*Fs)

#Else
else:
    print ('Please input a Stereo or Mono file')
#return 1
'''


plt.title('MFCC Analysis')
plt.subplot(1,1,1); plt.plot(F[9,:]); plt.xlabel('Frame no'); plt.ylabel('MFCC');
plt.subplot(1,1,1); plt.plot(F[10,:]); plt.xlabel('Frame no'); plt.ylabel('MFCC 2');
plt.subplot(1,1,1); plt.plot(F[11,:]); plt.xlabel('Frame no'); plt.ylabel('MFCC 3');
plt.subplot(1,1,1); plt.plot(F[12,:]); plt.xlabel('Frame no'); plt.ylabel('MFCC 4');
plt.subplot(1,1,1); plt.plot(F[13,:]); plt.xlabel('Frame no'); plt.ylabel('MFCC 5');
plt.subplot(1,1,1); plt.plot(F[14,:]); plt.xlabel('Frame no'); plt.ylabel('MFCC 6');


plt.show()




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
