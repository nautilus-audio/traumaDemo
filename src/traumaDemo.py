#!/usr/bin/python
'''
Anxiety = Red
Depression = Blue
PTSD = Green
Control = Yellow

Next Steps:
- Plot Data to Graph, Add Styling
- try, catch
- point to audioFiles directory
- make program run faster

audioFiles = ["PTSD_female.wav", "Anxiety_female.wav", "Depression_male.wav", "Depression_male2_JB.wav", "Depression_male3_JB.wav", "Control_male.wav", "Control_Male2.wav", "Depression_female.wav", "Depression_female2.wav", "Depression_female3.wav", "PTSD_male.wav", "Anxiety_male.wav", "Anxiety_male2.wav"]

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
        red = 'ro'
        blue = 'bo'
        green = 'go'
        yellow = 'yo'
        
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
            if frqs[0] == 0.0 and frqs[1] != 0.0:
                frqs.remove(0.0)
                firstFormantValues.append(frqs[0])
                secondFormantValues.append(frqs[1])
                print audioFiles[i].rstrip('.wav'), frqs[0], frqs[1] #Trace
                
                try:
                    formants.write("{} \t\t\t {} \t\t\t {} \n".format(audioFiles[i].rstrip('.wav'), frqs[0], frqs[1]))
                except:
                    print("Something went wrong when writing to the file.")
            
            elif frqs[0] == 0.0 and frqs[1] == 0.0:
                frqs.remove(0.0)
                firstFormantValues.append(frqs[1])
                secondFormantValues.append(frqs[2])
                print audioFiles[i].rstrip('.wav'), frqs[1], frqs[2] #Trace
                
                try:
                    formants.write("{} \t\t {} \t\t\t {} \n".format(audioFiles[i].rstrip('.wav'), frqs[1], frqs[2]))
                except:
                        print("Something went wrong when writing to the file.")
            else:
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
