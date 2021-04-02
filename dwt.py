import numpy as np
import cv2
import pywt
import copy
from numpy import zeros
from numpy import diag
from helpers import lsbVal, bitToInt, bitToWord, intToBit, wordToBit

class DWT:
    def encode(self, img, msg):
        blue, green, red = cv2.split(img) 
        bitMessage = wordToBit(msg)
        bitLenght = len(bitMessage)
        index = 0

        coeffsr = pywt.dwt2(red, 'haar')
        cAr, (cHr, cVr, cDr) = coeffsr
        
        coeffsg = pywt.dwt2(green, 'haar')
        cAg, (cHg, cVg, cDg) = coeffsg

        coeffsb = pywt.dwt2(blue, 'haar')
        cAb, (cHb, cVb, cDb) = coeffsb

        cArResult = copy.deepcopy(cAr)
        cAgResult = copy.deepcopy(cAg)
        cAbResult = copy.deepcopy(cAb)

        for i in range(len(cAr)):
            for j in range(len(cAr)):
                # red
                if index < bitLenght:
                    lsbPixel = intToBit(int(cAr[i,j]))[-2]
                    cArResult[i,j] = cAr[i,j] + lsbVal(bitMessage[index], lsbPixel)
                    index += 1
                # green
                if index < bitLenght:
                    lsbPixel = intToBit(int(cAg[i,j]))[-2]
                    cAgResult[i,j] = cAg[i,j] + lsbVal(bitMessage[index], lsbPixel)
                    index += 1
                # blue
                if index < bitLenght:
                    lsbPixel = intToBit(int(cAb[i,j]))[-2]
                    cAbResult[i,j] = cAb[i,j] + lsbVal(bitMessage[index], lsbPixel)
                    index += 1

        coeffsr2 = cArResult, (cHr, cVr, cDr)
        idwr = pywt.idwt2(coeffsr2,'haar')
        idwr = np.uint8(idwr)

        coeffsg2 = cAgResult, (cHg, cVg, cDg)
        idwg = pywt.idwt2(coeffsg2,'haar')
        idwg = np.uint8(idwg)

        coeffsb2 = cAbResult, (cHb, cVb, cDb)
        idwb = pywt.idwt2(coeffsb2,'haar')
        idwb = np.uint8(idwb)

        ImageResult = cv2.merge((idwb,idwg,idwr))
        
        return ImageResult


    def decode(self, img):
        blue, green, red = cv2.split(img)
        coeffsr = pywt.dwt2(red, 'haar')
        cAr, (cHr, cVr, cDr) = coeffsr
        
        coeffsg = pywt.dwt2(green, 'haar')
        cAg, (cHg, cVg, cDg) = coeffsg

        coeffsb = pywt.dwt2(blue, 'haar')
        cAb, (cHb, cVb, cDb) = coeffsb
        bit = []

        for i in range(len(cAr)):
            for j in range(len(cAr)):
                if len(intToBit(int(cAr[i,j]))) > 2:
                    bit.append(intToBit(int(cAr[i,j]))[-2])
                else:
                    bit.append('0')

                if len(intToBit(int(cAg[i,j]))) > 2:
                    bit.append(intToBit(int(cAg[i,j]))[-2])
                else:
                    bit.append('0')

                if len(intToBit(int(cAb[i,j]))) > 2:
                    bit.append(intToBit(int(cAb[i,j]))[-2])
                else:
                    bit.append('0')
        
        return bitToWord(bit)
