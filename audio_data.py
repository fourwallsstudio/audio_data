import os
import csv
import numpy as np
import librosa
from random import shuffle

class Data:

    def get_data():
        classes = ['house', 'techno']
        paths = ['./house/split/', './techno/split/']

        samples = []
        y = []

        for i in [0,1]:
            files = os.listdir(paths[i])

            for f in files:
                if not f.endswith(".mp3"): continue
                print(f)

                sound, sr = librosa.load(paths[i]+f, mono=True) 
                
                mfcc = librosa.feature.mfcc(sound, sr)
                # mfcc = np.pad(mfcc, ((0,0),(0,80-len(mfcc[0]))), mode='constant', constant_values=0)

                samples.append(np.array(mfcc))
                y.append(classes[i])

        zipped = list(zip(samples, y))
        shuffle(zipped)
        data = list(zip(*zipped)) # unzip

        return data

    def save_to_csv(data):
        X, Y = data

        with open('samples.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)

            for x in X:
                writer.writerow(x)

        with open('classifiers.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)

            for y in Y:
                writer.writerow([y])
       
# data = Data.get_data()
# print(data)
# Data.save_to_csv(data)
