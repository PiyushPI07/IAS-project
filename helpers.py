import cv2
import numpy as np

def wordToBit(words):    
    result = []
    for c in words:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def bitToWord(bits):      
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    flag = ''.join(chars)
    return flag

def intToBit(val):            
    result = bin(val)
    bitArray = list(map(int, result[2:]))
    bitArray.insert(0, 0)
    return bitArray

def bitToInt(bit):          
    val = ''.join(str(e) for e in bit)
    result = int(val, 2)
    return result

def lsbVal(a, b):
    result = 0
    if a == b:
        result = 0
    elif a == 1 and b == 0:
        result = 2
    elif a == 0 and b == 1:
        result = - 2
    return result