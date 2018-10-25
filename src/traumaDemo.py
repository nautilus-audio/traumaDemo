#!/usr/bin/python
'''

Next Steps:
- optimize
'''

from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt
import os, sys
import matplotlib.pyplot as style
#style.use('ggplot')

#Define Global Variables
path = "/Users/kamilahmitchell/Desktop/C++, Python & Vsts/Neurolex/traumaDemo/Audio Files"
dir = os.listdir(path)

class PerformOperation(object):
    
    i = 0
    
    def __init__(self, dir, audioFiles, i):
        self.dir = dir
        self.audioFiles = audioFiles
        self.i = i

    def readFiles(self):
        audioFiles = []
        for file in dir:
            if file.endswith(".wav"):
                audioFiles.append(file)
        print audioFiles #Trace
        return audioFiles

    def findFormants(audioFiles, i):


        #Define Variables
        red = 'ro' #Anxiety = Red
        blue = 'bo' #Depression = Blue
        green = 'go' #PTSD = Green
        yellow = 'yo' #Control = Yellow
        
        #Arrays to store colors, F1 & F2 Values
        plotColor = []
        firstFormantValues = []
        secondFormantValues = []
        
        #Open and Write to JSON audioFiles
        try:
            formants = open('formantData.json','w')
            formants.write("audioFiles Name: \t\t\t\t F1 (Hz): \t\t\t\t F2 (Hz): \n\n")
        except:
            print("Something went wrong when opening the file.")

        for i in range(len(audioFiles)):
            #Import & Analyze Audio Signal
            [Fs, x] = audioBasicIO.readAudioFile(audioFiles[i]);
            
            #Calculate Formant Frequencies
            frqs = audioFeatureExtraction.phormants(x[:,0], Fs);

            #Delete Empty Values, add Data to F1 F2 arrays
            #for i in range(len(frqs)-1):
            if 0.0 in frqs: frqs.remove(0.0)
            if 0.0 in frqs: frqs.remove(0.0)
            firstFormantValues.append(frqs[0])
            secondFormantValues.append(frqs[1])
            print audioFiles[i].rstrip('.wav'), frqs[0], frqs[1] #Trace
                    
            try:
                formants.write("{} \t\t\t {} \t\t\t {} \n".format(audioFiles[i].rstrip('.wav'), frqs[0], frqs[1]))
            except:
                print("Something went wrong when writing to the file.")
        
            #Assign Plot Color to Sample Type
            if  "PTSD" in audioFiles[i]:
                plotColor.append(green)
            elif "Depression" in audioFiles[i]:
                plotColor.append(blue)
            elif "Anxiety" in audioFiles[i]:
                plotColor.append(red)
            elif "Control" in audioFiles[i]:
                plotColor.append(yellow)
            else:
                print "Error, invalid voice sample entered"

            try:
                plt.plot(firstFormantValues[i], secondFormantValues[i], plotColor[i]);
            except:
                print("Something went wrong when plotting the data.")
                #data=[audioFiles][firstFormantValues][secondFormantValues]

            #firstFormantValues.sort();
            #plt.subplot(2,1,1);

        return formants

    #Call Functions
    audioFiles = readFiles(dir);
    formants = findFormants(audioFiles, i);

    #Close JSON File
    formants.close()

    #Style Plot and Save to JPG
    plt.axis([300, 900, 800, 2000])
    plt.title('Formant Values')
    plt.xlabel('F1 Frequency (Hz)');
    plt.ylabel('F2 Frequency (Hz)');
    plt.grid()
    plt.savefig('F1_F2_Values.png')
    plt.show()
