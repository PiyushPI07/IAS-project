from dwt import DWT
from dct import DCT
from lsb import LSB
import os
from PIL import Image
import cv2

c = input("Press 1 for LSB, 2 for DCT, 3 for DWT, any other key to exit\n")
if c == "1":
    lsb = LSB()
    os.chdir("Original_image/")
    orig_image_name = input("Enter the name of the image with extension\n")
    image = Image.open(orig_image_name)
    print("Image Details: \n Description: {}\nMode: {}".format(image, image.mode))
    message = input("Enter the message you want to hide:\n")
    os.chdir("..")
    os.chdir("Encoded_image/")
    encoded_image = lsb.encode(image, message)
    print("Message Encoded inside the image successfully!\n")
    encoded_image_name = "lsb_"+orig_image_name
    encoded_image.save(encoded_image_name)
    print("Saved encoded image with name: {}".format(encoded_image_name))
    decoded_message  = lsb.decode(encoded_image)
    os.chdir("..")
    os.chdir("Decoded_output/")
    file = open("lsb_decoded_secret_message_{}.txt".format(orig_image_name), "w")
    file.write(decoded_message)
    file.close()
    print("Decoded secret message saved successfully!")
if c=="2":
    dct = DCT()
    os.chdir("Original_image/")
    orig_image_name = input("Enter the name of the image with extension\n")
    image = cv2.imread(orig_image_name, cv2.IMREAD_UNCHANGED)
    message = input("Enter the message you want to hide:\n")
    os.chdir("..")
    os.chdir("Encoded_image/")
    encoded_image = dct.encode(image, message)
    encoded_image_name = "dct_"+orig_image_name
    cv2.imwrite(encoded_image_name, encoded_image)
    print("Saved encoded image with name: {}".format(encoded_image_name))
    decoded_message  = dct.decode(encoded_image)
    os.chdir("..")
    os.chdir("Decoded_output/")
    file = open("dct_decoded_secret_message_{}.txt".format(orig_image_name), "w")
    file.write(decoded_message)
    file.close()
    print("Decoded secret message saved successfully!")
if c=="3":
    dwt = DWT()
    os.chdir("Original_image/")
    orig_image_name = input("Enter the name of the image with extension\n")
    image = cv2.imread(orig_image_name, cv2.IMREAD_UNCHANGED)
    message = input("Enter the message you want to hide:\n")
    os.chdir("..")
    os.chdir("Encoded_image/")
    encoded_image = dwt.encode(image, message)
    encoded_image_name = "dwt_"+orig_image_name
    cv2.imwrite(encoded_image_name, encoded_image)
    print("Saved encoded image with name: {}".format(encoded_image_name))
    decoded_message  = dwt.decode(encoded_image)[:len(message)]
    os.chdir("..")
    os.chdir("Decoded_output/")
    file = open("dwt_decoded_secret_message_{}.txt".format(orig_image_name), "w")
    file.write(decoded_message)
    file.close()
    print("Decoded secret message saved successfully!")
else:
    exit()