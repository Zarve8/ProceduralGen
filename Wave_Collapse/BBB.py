from PIL import Image
import numpy as np

block_size = 3
img_size = 64

blocks_names = []
blocks_im = []
blocks_map = []
rules = set()


def fill_map():
    global blocks_map
    global block_size
    global img_size
    l = int(img_size/block_size)
    for i in range(0, l):
        a = []
        for j in range(0, l):
            a.append(0)
        blocks_map.append(a)


def to_map(file_dir):
    global img_size
    global block_size
    global blocks_names
    global blocks_im
    global blocks_map
    img = Image.open(file_dir)
    pixels = img.load()
    for i in range(0, int(img_size/block_size)):
        for j in range(0, int(img_size/block_size)):
            block = []
            for k in range(0, block_size):
                a = []
                for m in range(0, block_size):
                    a.append(pixels[i*block_size+k, j*block_size+m])
                block.append(a)
            try:
                ind = blocks_im.index(block)
                blocks_map[i][j] = blocks_names[ind]
            except:
                blocks_im.append(block)
                c = chr(65 + len(blocks_names))
                blocks_names.append(c)
                blocks_map[i][j] = c


def pout():
    global blocks_map
    global block_size
    global img_size
    l = int(img_size / block_size)
    for i in range(0, l):
        for j in range(0, l):
            print(blocks_map[i][j], end=" ")
        print(end="\n")


def parse_rules():
    global block_size
    global img_size
    global blocks_map
    global rules
    l = int(img_size/block_size)
    for i in range(0, l):
        for j in range(0, l):
            if(i + 1 < l):
                rules.update([(blocks_map[i][j], blocks_map[i+1][j], "up")])
                rules.update([(blocks_map[i + 1][j], blocks_map[i][j], "down")])
            if (i - 1 > 0):
                rules.update([(blocks_map[i - 1][j], blocks_map[i][j], "up")])
                rules.update([(blocks_map[i][j], blocks_map[i - 1][j], "down")])
            if (j + 1 < l):
                rules.update([(blocks_map[i][j], blocks_map[i][j+1], "left")])
                rules.update([(blocks_map[i][j+1], blocks_map[i][j], "right")])
            if (j - 1 > 0):
                rules.update([(blocks_map[i][j], blocks_map[i][j-1], "right")])
                rules.update([(blocks_map[i][j-1], blocks_map[i][j], "left")])
    rules = list(rules)


def get_rules():
    global rules
    return rules


def get_possible():
    global blocks_names
    return tuple(blocks_names)


def imout(new_map, size):
    global blocks_im
    global block_size
    img = Image.new(mode="RGB", size=(size*block_size, size*block_size), color="black")
    pixels = img.load()
    for i in range(0, size):
        for j in range(0, size):
            ind = ord(new_map[i][j]) - 65
            block = blocks_im[ind]
            for k in range(0, block_size):
                for m in range(0, block_size):
                    pixels[i*block_size+k, j*block_size+m] = block[k][m]
    img.save("Field.png")


def main(file_dir):
    global rules
    fill_map()
    to_map(file_dir)
    parse_rules()
