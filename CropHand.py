import cv2
import numpy as np
from HandLandmarkModule import handDetector

class CropHand():
    def elements(self, array):
        return array.ndim and array.size

    def crop(self, img):
        hand = handDetector()
        positions = hand.landmarkPositions(img)
        positions = np.array(positions)

        cropped_image = []
        cropped_image = np.array(cropped_image)

        if self.elements(positions):
            min_y = min(positions[:, 2])
            max_y = max(positions[:, 2])
            min_x = min(positions[:, 1])
            max_x = max(positions[:, 1])

            cropped_image = img[min_y - 25 : max_y + 25, min_x - 25 : max_x + 25]

        return cropped_image



