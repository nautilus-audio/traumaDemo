
#!/usr/bin/python

from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt
import matplotlib.pyplot as style

#Define Global Variables
FILE = ["PTSD_female.wav", "Anxiety_female.wav", "Depression_male.wav", "Depression_male2_JB.wav", "Depression_male3_JB.wav"]
length = len(FILE)-1
i = 0

def findFormants(FILE, i, length):

    #Define Variables
    nfft = 256
    X = 32
    nceps = 64

    while i <= length:
        #Import & Analyze Audio Signal
        [Fs, x] = audioBasicIO.readAudioFile(FILE[i]);
    
        #Calculate Formant Frequencies
        frqs = audioFeatureExtraction.phormants(x[:,0], Fs);
        
        #print frqs
        
        
        if frqs[0] == 0.0 and frqs[1] != 0.0:
            print FILE[i], frqs[1]
        elif frqs[0] == 0.0 and frqs[1] == 0.0:
                print FILE[i], frqs[2]
        else:
            print FILE[i], frqs[0]
        
        '''
            Next Steps:
            - Add first formant values from frqs[] to new array
            - Sort Array from lowest to highest values
            - Plot Data to Graph
        '''
        
        #Visualize Data
        plt.title('Formant Values')
        #plt.subplot(1,1,1); plt.plot(F[9,:]); plt.xlabel('Frame no'); plt.ylabel('MFCC');
        #plt.subplot(1,1,1); plt.plot(ceps[:,0]); plt.xlabel('Frame no'); plt.ylabel('Freq (Hz)');
        plt.subplot(1,1,1); plt.plot(frqs); plt.xlabel('Frame no'); plt.ylabel('Freq (Hz)');
        
        i += 1

    #[HR, f0] = audioFeatureExtraction.stHarmonic(x[:,0], Fs)

    #Calculate MFCCs
    [fbank, freqs] = audioFeatureExtraction.mfccInitFilterBanks(Fs, nfft);
    ceps = audioFeatureExtraction.stMFCC(X, fbank, nceps);

    return frqs, x


#Call Functions
[frqs, x] = findFormants(FILE, i, length);
#print frqs

plt.show()





