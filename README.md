# traumaDemo
## [Neurolex Laboratories](https://github.com/NeuroLexDiagnostics) TRIBE 3 software demo 
Python script that calculates first (F1) and second (F2) formant values of an array of voice samples, outputs the data to a JSON file, plots data to graph in matplotlib and renders a png file to visualize the data. 
Formants calculated using [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis).

### Project Goals: 
Use voice analysis to calculate Formant Frequencies of Voice Samples of PTSD, Anxiety and Depression patients (as well as a control set) to compare data on these trauma-related disorders. Implement in Python program.

### Premise: 
Anxiety and depression are more common mental disorders, and the diagnosis of these can cause PTSD to be overlooked. It is very common for PTSD patients to experience anxiety and depression as well. Early detection can prevent the compilation of diseases due to the long-term effects of living without proper treatment. A formant is a concentration of acoustic energy around a particular frequency, or a resonance in the vocal tract. Formants occur at roughly 1000Hz intervals.

### Hypothesis: 
Depression samples will have lower frequencies, PTSD samples will have the highest. This is based off of past research suggesting that formant frequencies of schizophrenia patients are lower during negative symptoms (apathy, lack of emotion, poor or non-existent social functioning) and higher during positive symptoms (hallucinations, delusions, racing thoughts). 

### Results
![alt text](https://github.com/imABEING/traumaDemo/blob/master/F1_F2_Values.png "Plot")

Yellow = Control
Blue = Depressio
Red = Anxiety
Green = PTSD
