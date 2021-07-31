import os
import cv2


class LoadData():
    def __init__(self,
                 mainPath = '/Users/Amir/Downloads/Dataset/',
                 paths = ['FiestForward',
                          'FiestUpward',
                          'FigersCrossed',
                          'OK',
                          'Palm',
                          'PointFinger',
                          'RocknRoll',
                          'ThumbsDown',
                          'ThumbsUp',
                          'Victory',
                          'Yeaaah']):
        self.mainPath = mainPath
        self.paths = paths

    def load(self):
        totalFiles = 0
        X = []
        Y = []
        
        for i in range(len(self.paths)):
            path = self.mainPath + self.paths[i]

            # Counting the number of images in each directory
            for base, dirs, files in os.walk(path):
                print('Searching in : ',base)
                for Files in files:
                    totalFiles += 1

            for j in range(totalFiles):
                X.append(cv2.imread(path + '/images/' + str(j + 1) + '.jpg'))
                Y.append(i)

        return X, Y





