
#!/usr/bin/python
'''
Use Feature Extraction from pyAudioAnalyis to analyze voice samples with MFCC. Calculate to get fundamental frequency. Calculate formant from F0. Then calculate first formant using the average vocal human tract length, and subsequent formants.
'''


from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt
import matplotlib.pyplot as style

def findFormants():

    #Define Variables
    nfft = 256
    X = 32
    nceps = 64

    #Import & Analyze Audio Signal
    [Fs, x] = audioBasicIO.readAudioFile("PTSD_female2.wav");

    #[HR, f0] = audioFeatureExtraction.stHarmonic(x[:,0], Fs)

    #Calculate Formant Frequencies
    frqs = audioFeatureExtraction.phormants(x[:,0], Fs);

    #Calculate MFCCs
    [fbank, freqs] = audioFeatureExtraction.mfccInitFilterBanks(Fs, nfft);
    ceps = audioFeatureExtraction.stMFCC(X, fbank, nceps);

    return frqs


#Call Functions
frqs = findFormants();
print frqs


#Visualize Data
plt.title('MFCC Analysis')
#plt.subplot(1,1,1); plt.plot(F[9,:]); plt.xlabel('Frame no'); plt.ylabel('MFCC');
#plt.subplot(1,1,1); plt.plot(ceps[:,0]); plt.xlabel('Frame no'); plt.ylabel('Freq (Hz)');
plt.subplot(1,1,1); plt.plot(frqs); plt.xlabel('Frame no'); plt.ylabel('Freq (Hz)');


plt.show()


