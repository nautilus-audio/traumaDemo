
#!/usr/bin/python

from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt
import matplotlib.pyplot as style

#Define Global Variables
FILE = ["PTSD_female.wav", "Anxiety_female.wav", "Depression_male.wav", "Depression_male2_JB.wav", "Depression_male3_JB.wav"]
firstFormantValues = []
length = len(FILE)-1
i = 0


def findFormants(FILE, i, length, firstFormantValues):

    #Define Variables
    nfft = 256
    X = 32
    nceps = 64

    while i <= length:
        #Import & Analyze Audio Signal
        [Fs, x] = audioBasicIO.readAudioFile(FILE[i]);
    
        #Calculate Formant Frequencies
        frqs = audioFeatureExtraction.phormants(x[:,0], Fs);
        
        #Delete Empty Values, add Formant Values to new array, Print File Name and Formant Value
        '''
            if FILE[i] == "female"
                plot color...
            if FILE[i] == "male"
            if FILE[i] == "PTSD"
            if FILE[i] == "Depression"
            if FILE[i] == "Anxiety"
            if FILE[i] == "Control"
        '''
        
        if frqs[0] == 0.0 and frqs[1] != 0.0:
            del frqs[0]
            firstFormantValues.append(frqs[0])
            print FILE[i], frqs[0]
        elif frqs[0] == 0.0 and frqs[1] == 0.0:
            del frqs[1]
            firstFormantValues.append(frqs[1])
            print FILE[i], frqs[1]
        else:
            firstFormantValues.append(frqs[0])
            print FILE[i], frqs[0]
        
        #firstFormantValues.sort();
        '''
            Next Steps:
            - Plot Data to Graph, Add Styling, Make Scatter Plot?
        '''
        
        #Visualize Data
        plt.title('Formant Values')
        #plt.subplot(1,1,1); plt.plot(frqs); plt.xlabel('Frame no'); plt.ylabel('Freq (Hz)');
        plt.subplot(1,1,1); plt.plot(firstFormantValues); plt.xlabel('Sample no'); plt.ylabel('Freq (Hz)');
        
        i += 1

    #[HR, f0] = audioFeatureExtraction.stHarmonic(x[:,0], Fs)

    #Calculate MFCCs
    [fbank, freqs] = audioFeatureExtraction.mfccInitFilterBanks(Fs, nfft);
    ceps = audioFeatureExtraction.stMFCC(X, fbank, nceps);

    return frqs, x, firstFormantValues, FILE


#Call Functions
[frqs, x, firstFormantValues, FILE] = findFormants(FILE, i, length, firstFormantValues);
#print firstFormantValues


plt.show()





