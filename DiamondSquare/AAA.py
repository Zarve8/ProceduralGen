import numpy as np
import CCC as rd


precise = 255
ind = 1
num = 0
mul = 0.5


def process_bar(a):
    global num
    while num < int(a/10):
        print("⬜", end="")
        num +=1
        pass


def diamond(s, size, l):
    global precise
    global ind
    global mul
    i = 1
    while i < ind:
        j = 1
        while j < ind:
            sum = s[(i - 1) * l][(j - 1) * l]
            sum += s[(i - 1) * l][(j + 1) * l]
            sum += s[(i + 1) * l][(j - 1) * l]
            sum += s[(i + 1) * l][(j + 1) * l]
            sum /= 4
            sum *= (1-mul)
            sum += mul*(rd.randint(0, 2 * precise) / precise - 1)
            s[i * l][j * l] = sum
            j += 2
        i += 2


def square(s, size, l):
    global precise
    global mul
    global ind
    i = 1
    while i < ind:
        sum = s[(i+1)*l][0]
        sum += s[(i-1)*l][0]
        sum += s[i * l][l]
        sum += s[i * l][size-l-1]
        sum /= 4
        sum *= (1-mul)
        sum += mul*(rd.randint(0, 2 * precise) / precise - 1)
        s[i*l][0] = sum
        sum = s[(i + 1) * l][size-1]
        sum += s[(i - 1) * l][size-1]
        sum += s[i * l][size-l-1]
        sum += s[i * l][l]
        sum /= 4
        sum *= (1-mul)
        sum += mul * (rd.randint(0, 2 * precise) / precise - 1)
        s[i * l][size-1] = sum
        sum = s[0][(i + 1) * l]
        sum += s[0][(i - 1) * l]
        sum += s[l][i * l]
        sum += s[size - l - 1][i * l]
        sum /= 4
        sum *= (1-mul)
        sum += mul * (rd.randint(0, 2 * precise) / precise - 1)
        s[0][i * l] = sum
        sum = s[size - 1][(i + 1) * l]
        sum += s[size - 1][(i - 1) * l]
        sum += s[size - l - 1][i * l]
        sum += s[l][i * l]
        sum /= 4
        sum *= (1-mul)
        sum += mul * (rd.randint(0, 2 * precise) / precise - 1)
        s[size - 1][i * l] = sum
        i += 2
    i = 1
    while i < ind:
        j = 2
        while j < ind:
            sum = s[(i - 1) * l][j * l]
            sum += s[(i + 1) * l][j * l]
            sum += s[i * l][(j - 1) * l]
            sum += s[i * l][(j + 1) * l]
            sum /= 4
            sum *= (1-mul)
            sum += mul*(rd.randint(0, 2 * precise) / precise - 1)
            s[i * l][j * l] = sum
            sum = s[(j - 1) * l][i * l]
            sum += s[(j + 1) * l][i * l]
            sum += s[j * l][(i - 1) * l]
            sum += s[j * l][(i + 1) * l]
            sum /= 4
            sum *= (1-mul)
            sum += mul * (rd.randint(0, 2 * precise) / precise - 1)
            s[j * l][i * l] = sum
            j += 2
        i += 2


def main(s, size):
    print("Diamond_square started process\n[", end="")
    global precise
    global ind
    global mul
    s[0][0] = rd.randint(0, 2 * precise) / precise - 1
    s[0][size-1] = rd.randint(0, 2 * precise) / precise - 1
    s[size-1][0] = rd.randint(0, 2 * precise) / precise - 1
    s[size-1][size-1] = rd.randint(0, 2 * precise) / precise - 1
    ind = 2
    l = int((size-1)/2)
    while ind < size:
        diamond(s, size, l)
        square(s, size, l)
        process_bar(100*ind/size)
        ind *= 2
        mul /= 2
        l = int(l/2)
    process_bar(100)
    print("]")
    return s

