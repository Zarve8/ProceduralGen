from PIL import Image
import numpy as np

def imout(s, size):
    print("Started writing image")
    img = Image.new(mode="RGB", size=(size, size), color="red")
    pixels = img.load()
    for i in range(0, size):
        for j in range(0, size):
            pixels[i,j] = (int((s[i][j]+1)*127), int((s[i][j]+1)*127), int((s[i][j]+1)*127))
    img.save("Image.png")

def objout(s, size):
    h = 1000
    fout = open("Lanscape.obj", "w")
    print("Started writing obj")
    v = []
    f = []
    for i in range(0, size):
        for j in range(0, size):
            fout.write("v "+str(i*10)+" "+str(j*10)+" "+str(s[i][j]*h)+"\n")
    for i in range(0, size-1):
        for j in range(0, size-1):
            fout.write("f " + str(i * (size) + j + 1) + " " + str((i+1)* (size) + j + 1) + " " + str((i) * (size) + j + 2)+"\n")
            fout.write("f " + str((i + 1) * (size) + j + 1) + " " + str((i + 1) * (size) + j + 2) + " " + str(i * (size) + j + 2) + " " + "\n")

