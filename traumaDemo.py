
#!/usr/bin/python
'''
Anxiety = Red
Depression = Blue
PTSD = Green
Control = Yellow

Next Steps:
- Plot Data to Graph, Add Styling
- F1 = x-axis, F2 = y-axis?
'''

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
    red = 'ro'
    blue = 'bo'
    green = 'go'
    yellow = 'yo'
    
    #Arrays to store colors, F1 % F2 Values
    plotColor = []
    firstFormantValues = []
    secondFormantValues = []
    
    #Open and Write to JSON file
    formants = open('formantData.json','w')
    formants.write("File Name: \t\t\t\t F1 (Hz): \t\t\t\t F2 (Hz): \n\n")

    while i <= length:
        #Import & Analyze Audio Signal
        [Fs, x] = audioBasicIO.readAudioFile(FILE[i]);

        #Calculate Formant Frequencies
        frqs = audioFeatureExtraction.phormants(x[:,0], Fs);

        #Delete Empty Values, add Data to new array
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
            plotColor.append(green)
        elif "Depression" in FILE[i]:
            plotColor.append(blue)
        elif "Anxiety" in FILE[i]:
            plotColor.append(red)
        elif "Control" in FILE[i]:
            plotColor.append(yellow)

        plt.plot(firstFormantValues[i], secondFormantValues[i], plotColor[i]);

        #firstFormantValues.sort();
        #plt.subplot(2,1,1);
        
        i += 1
                   
    return frqs, x, firstFormantValues, secondFormantValues, formants


#Call Functions
[frqs, x, firstFormantValues, secondFormantValues, formants ] = findFormants(FILE, i, length);

#Close Text File
formants.close()

#Style Plot and Save to JPG
plt.axis([300, 700, 800, 1800])
plt.title('Formant Values')
plt.xlabel('F1 Frequency (Hz)');
plt.ylabel('F2 Frequency (Hz)');
plt.grid()
plt.savefig('F1_F2_Values.png')
plt.show()





