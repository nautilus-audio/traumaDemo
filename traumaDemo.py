
#!/usr/bin/python


from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction

#Import & Analyze Audio Signal
[Fs, x] = audioBasicIO.readAudioFile("OSIRIS_Motif.wav");
#F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs);
F = audioFeatureExtraction.stFeatureExtraction(x[:,0], Fs, 0.050*Fs, 0.025*Fs)






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
