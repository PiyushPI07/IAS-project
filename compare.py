from scipy import signal
import os
import cv2
import numpy as np
import math
class Compare():
    def correlation(self, img1, img2):
        return signal.correlate2d (img1, img2)
    def meanSquareError(self, img1, img2):
        error = np.sum((img1.astype('float') - img2.astype('float')) ** 2)
        error /= float(img1.shape[0] * img1.shape[1]);
        return error
    def psnr(self, img1, img2):
        mse = self.meanSquareError(img1,img2)
        if mse == 0:
            return 100
        PIXEL_MAX = 255.0
        return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


compare = Compare()
original_image_path = input("Enter name of original image with extension: \n")
encoded_image_path = input("Enter name of incoded image with extension: \n")
orig_image = cv2.imread("Original_image/"+original_image_path, cv2.COLOR_BGR2RGB)
enc_image = cv2.imread("Encoded_image/"+encoded_image_path, cv2.COLOR_BGR2RGB)
orig_image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2GRAY)
enc_image = cv2.cvtColor(enc_image, cv2.COLOR_BGR2GRAY)
print("-----------------------------------------------------------------------")
print("Correlation:                     {}".format(compare.correlation(orig_image, enc_image)))

print("-----------------------------------------------------------------------")
print("Mean Square Error:               {}".format(compare.meanSquareError(orig_image, enc_image)))

print("-----------------------------------------------------------------------")
print("Peak Signal to Noise Ratio(PSNR) {}".format(compare.psnr(orig_image, enc_image)))
print("-----------------------------------------------------------------------")
