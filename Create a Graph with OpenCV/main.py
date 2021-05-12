#import cv2          $ pip install opencv-python
#import numpy        $ pip install numpy
#import matplotlib   $ pip install matplotlib
#import argparse     (preinstalled)
#import os           (preinstalled)
#import json         (preinstalled)
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
import json

if __name__ == "__main__":
    #percentage calculator
    def percentage(percent, whole):
        return (percent * 100) / whole

    #loadingscreen
    def loadingscreen(times, p_lenght, c):
        progress = (c / times) * 100 + 1
        b = p_lenght / 100
        if c % p_lenght == 0:
            os.system('cls')
            print("Processing...     (This can take a wihle.)")
            print("[", end = '')
            for i in range(int(b * progress)):
                print("=", end = '')

            for i in range(int(p_lenght - b * progress)):
                print("-", end = '')
            print("]")

    #--image command
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the input image")
    args = vars(ap.parse_args())

    #set image
    img = cv2.imread(args["image"], cv2.IMREAD_UNCHANGED)

    #get reselution
    dimensions = img.shape
    height = img.shape[0]
    width = img.shape[1]

    #calculate pixel
    reselution = height * width

    #set image to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #quest input
    times = int(input("Times from input to 255 (Max 255): "))

    #cap input to 255
    if times > 255:
        times = 255
    timesa = times

    #delet json if exists
    if os.path.exists('file.json'):
        os.remove('file.json') 

    #write json
    a = 255
    c = 1
    with open('file.json', 'a') as outfile:
        outfile.write("{\n" + "\"times\"" + " : " + str(times) + ",\n")
        for i in range(times):
            timesa -= 1
            loadingscreen(times, 30, c)
            ret, thresh = cv2.threshold(gray, a, 255, cv2.THRESH_BINARY)
            px = np.sum(gray >= a)
            outfile.write("\"" + str(a) + "\"" + " : " + str(percentage(px, reselution)))
            if timesa > 0:
                outfile.write(",\n")
            else:
                outfile.write("\n")
            c += 1
            a -= 1
        outfile.write("}")
        outfile.close()

    #set x and y for graph
    json_file = open("file.json")
    f = json.load(json_file)
    numbera = f['times']
    x = []
    y = []
    a += 1
    for i in range(times):
        x.append(a)
        y.append(f[str(a)])
        a += 1

    #open graph
    plt.plot(x, y)
    plt.xlabel('RGB value from value 255')
    plt.ylabel('Persent')
    plt.show()
