import tlsh
import cv2
import os
import time
import imagehash
from PIL import Image

cam_port = 1
cam = cv2.VideoCapture(cam_port)
dimensions = (10, 10)

image1 = None
image2 = None
diff = 0

result, image2 = cam.read()
if not result:
    print("Error reading from webcam\n")
    exit()


# image2 = cv2.resize(image2, dimensions)

# cv2.imwrite("poop.png", image2)

# input()

while True:
    # print('''
    #         c to continue\n
    #         q to quit\n
    #       ''')
    # user_input = input("$: ")
    # if user_input == "q":
    #     break

    image1 = image2
    # time.sleep(1)
    result, image2 = cam.read()

    cv2.imwrite("temp1.png", image1)
    cv2.imwrite("temp2.png", image2)
    # image2 = cv2.resize(image2, dimensions)
    
    if not result:
        print("Error reading from webcam\n")
        exit()
    
    h1 = imagehash.average_hash(Image.open("temp1.png"))
    h2 = imagehash.average_hash(Image.open("temp2.png"))
    
    ph1 = imagehash.phash(Image.open("temp1.png"))
    ph2 = imagehash.phash(Image.open("temp2.png"))

    os.system('clear')
    print("ahash Hammond distance:\t\t" + str(h1-h2) + " \n")
    print("phash Hammond distance:\t\t" + str(ph1-ph2) + " \n")
    time.sleep(0.1)


    # h1 = tlsh.hash(image1)
    # h2 = tlsh.hash(image2)

    # assert tlsh.diff(h1,h1) == 0

    # score = tlsh.diff(h1,h2)
    # score2 = tlsh.diffxlen(h1,h2)

    # os.system('clear')
    # print("Image diff:\t\t" + str(score) + " \n")
    # print("Image diff no len:\t" + str(score2) + " \n")
    # time.sleep(0.2)



