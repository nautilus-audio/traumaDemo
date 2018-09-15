
#!/usr/bin/python
'''
Anxiety = Red
Depression = Blue
PTSD = Green
Control = Yellow
'''

from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt
import matplotlib.pyplot as style

#Define Global Variables
FILE = ["PTSD_female.wav", "Anxiety_female.wav", "Depression_male.wav", "Depression_male2_JB.wav", "Depression_male3_JB.wav"]
firstFormantValues = []
secondFormantValues = []
length = len(FILE)-1
i = 0



def findFormants(FILE, i, length, firstFormantValues, secondFormantValues):

    #Define Variables
    nfft = 256
    X = 32
    nceps = 64
    
    red = 'ro'
    blue = 'bo'
    green = 'go'
    yellow = 'yo'
    plotColor = ''
    dummy = ''
    
    #Open and Start JSON file
    formants = open('formantData.json','w')
    formants.write("File Name: \t\t\t\t F1 (Hz): \t\t\t\t F2 (Hz): \n")

    while i <= length:
        #Import & Analyze Audio Signal
        [Fs, x] = audioBasicIO.readAudioFile(FILE[i]);

        #Calculate Formant Frequencies
        frqs = audioFeatureExtraction.phormants(x[:,0], Fs);

        #Delete Empty Values, add Formant Values to new array, Print File Name and Formant Value
        if frqs[0] == 0.0 and frqs[1] != 0.0:
            del frqs[0]
            firstFormantValues.append(frqs[0])
            secondFormantValues.append(frqs[1])
            print FILE[i].rstrip('.wav'), frqs[0], frqs[1] #Trace
            formants.write("{} \t\t\t {} \t\t\t {} \n".format(FILE[i].rstrip('.wav'), frqs[0], frqs[1]))
        elif frqs[0] == 0.0 and frqs[1] == 0.0:
            del frqs[1]
            firstFormantValues.append(frqs[1])
            secondFormantValues.append(frqs[2])
            print FILE[i].rstrip('.wav'), frqs[1], frqs[2] #Trace
            formants.write("{} \t {} \t\t\t {} \n".format(FILE[i].rstrip('.wav'), frqs[1], frqs[2]))
        else:
            firstFormantValues.append(frqs[0])
            secondFormantValues.append(frqs[1])
            print FILE[i].rstrip('.wav'), frqs[0], frqs[1] #Trace
            formants.write("{} \t\t\t {} \t\t\t {} \n".format(FILE[i].rstrip('.wav'), frqs[0], frqs[1]))

        #Assign Plot Color to Sample Type
        if  "PTSD" in FILE[i]:
            plt.subplot(2,1,1); plt.plot(firstFormantValues, green);
            plt.subplot(2,1,2); plt.plot(secondFormantValues, green);
        elif "Depression" in FILE[i]:
            plt.subplot(2,1,1); plt.plot(firstFormantValues, blue);
            plt.subplot(2,1,2); plt.plot(secondFormantValues, blue);
        elif "Anxiety" in FILE[i]:
            plt.subplot(2,1,1); plt.plot(firstFormantValues, red);
            plt.subplot(2,1,2); plt.plot(secondFormantValues, red);
        elif "Control" in FILE[i]:
            plt.subplot(2,1,1); plt.plot(firstFormantValues, yellow);
            plt.subplot(2,1,2); plt.plot(secondFormantValues, yellow);

        #firstFormantValues.sort();
        '''
            Next Steps:
            - Plot Data to Graph, Add Styling, Make Scatter Plot?
            - F1 = x-axis, F2 = y-axis?
        '''
        
        plotColor = dummy
        
        i += 1

    #[HR, f0] = audioFeatureExtraction.stHarmonic(x[:,0], Fs)

    #Calculate MFCCs
    [fbank, freqs] = audioFeatureExtraction.mfccInitFilterBanks(Fs, nfft);
    ceps = audioFeatureExtraction.stMFCC(X, fbank, nceps);
    
#formants.write("{} \n".format(FILE[i])
        
    #formants.write("File Name: {} \t F1: {} \t F2: {} \n".format(FILE[i]-1, firstFormantValues[i-1], secondFormantValues[i-1]))
                   
    return frqs, x, firstFormantValues, secondFormantValues, formants


#Call Functions
[frqs, x, firstFormantValues, secondFormantValues, formants ] = findFormants(FILE, i, length, firstFormantValues, secondFormantValues);

#Close Text File
formants.close()

#plt.axis([0, length, 0, 800])
plt.title('Formant Values')
plt.xlabel('Sample no');
plt.ylabel('F1 Frequency (Hz)');
plt.show()





