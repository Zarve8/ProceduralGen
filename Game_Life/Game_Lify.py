import tkinter as tk
import time
import random
from PIL import Image, ImageTk
from copy import deepcopy
root = tk.Tk()


#setting image parameters
field_size = 16
block_size = 16
space_size = 4
delta_time = 1
rand = True

def RandList(size):
    s = []

    for i in range(0, size):
        a = []
        for j in range(0, size):
            a.append(random.randint(0, 1))
        s.append(a)
    return s


def LifeStage(s, img):
    s2 = deepcopy(s)
    for i in range(0, field_size):
        for j in range(0, field_size):
            e = 0
            if (s[(i + 1) % field_size][(j) % field_size] > 0):
                e += 1
            if (s[(i - 1) % field_size][(j) % field_size] > 0):
                e += 1
            if (s[(i) % field_size][(j + 1) % field_size] > 0):
                e += 1
            if (s[(i) % field_size][(j - 1) % field_size] > 0):
                e += 1
            if (s[(i + 1) % field_size][(j + 1) % field_size] > 0):
                e += 1
            if (s[(i - 1) % field_size][(j - 1) % field_size] > 0):
                e += 1
            if (s[(i + 1) % field_size][(j - 1) % field_size] > 0):
                e += 1
            if (s[(i - 1) % field_size][(j + 1) % field_size] > 0):
                e += 1
            if (s[i][j] > 0):
                if e < 2 or e > 3:
                    s[i][j] = 0
            else:
                if e == 3:
                    s[i][j] = 1

    # Convert to image from s to img
    pixels = img.load()
    for i in range(0, field_size):
        for j in range(0, field_size):
            if (s2[i][j] > 0):
                col = (0, 255, 0)
            elif (s2[i][j] < 0):
                col = (255, 0, 0)
            else:
                col = (0, 0, 0)
            for a in range(i * block_size + (i + 1) * space_size, (i + 1) * block_size + (i + 1) * space_size):
                for b in range(j * block_size + (j + 1) * space_size, (j + 1) * block_size + (j + 1) * space_size + 1):
                    pixels[a, b] = col
    return img


#input start data
if rand != 1:
    file = open("DataList.txt", "r")
    rows = file.read().splitlines()
    s = []
    for i in rows:
        s.append([int(bool(int(j))) for j in i.split()])
else:
    s = RandList(field_size)

#Calculating size
filed_size = len(s)
fsize = field_size*block_size+(field_size+1)*space_size

#creating init image
img = Image.new("RGB", (fsize, fsize), "grey")

#create frame to use
frame = tk.Frame(root)
frame.grid()

x = bool(1)
canvas = tk.Canvas(root, height=fsize, width=fsize)
while(x):
    time.sleep(delta_time)
    img = LifeStage(s, img)
    #delete canvas
    canvas.delete("all")
    #insert image
    photo = ImageTk.PhotoImage(img)
    image = canvas.create_image(0, 0, anchor='nw',image=photo)
    canvas.grid(row=2,column=1)
    root.update()


