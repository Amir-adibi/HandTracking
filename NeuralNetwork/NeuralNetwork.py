import keras
import cv2
from keras.models import Sequential
from keras.layers import Dense,  Activation
import numpy as np
from LoadDataset import LoadData

Data = LoadData()
X, Y = Data.load()


cv2.imshow('image', X[1])
cv2.waitKey(0)

label_map = ['Palm', 'Fiest forward', 'Fiest leftside', 'Fiest rightside',
             'Fiest upward', 'Finger Crossed', 'OK', 'Point finger',
             'Rock and roll', 'Thumbs down', 'Thumbs up', 'Victory', 'yeah']

