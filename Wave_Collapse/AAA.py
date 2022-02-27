import random
import BBB
from copy import deepcopy


arr = []
rules = [('S', 'S', "left"), ('S', 'S', "right"), ('S', 'S', "up"), ('S', 'S', "down"),
         ('L', 'L', "left"), ('L', 'L', "right"), ('L', 'L', "up"), ('L', 'L', "down"),
         ('W', 'W', "left"), ('W', 'W', "right"), ('W', 'W', "up"), ('W', 'W', "down"),
         ('S', 'L', "up"), ('S', 'L', "right"), ('L', 'S', "down"), ('L', 'S', "left"),
         ('S', 'W', "left"), ('S', 'W', "right"), ('S', 'W', "up"), ('S', 'W', "down"),
         ('W', 'S', "left"), ('W', 'S', "right"), ('W', 'S', "up"), ('W', 'S', "down")]

size = 16
num = size*size
possible_values = ('L', 'S', 'W')


def fout(arr):
    global size
    s = []
    f = open("output.txt", "w")
    for i in range(0, size):
        a = []
        for j in range(0, size):
            if (len(arr[i][j]) == 0):
                a.append('A')
            else:
                a.append(arr[i][j][0])
        s.append(a)
    BBB.imout(s, size)


def fout2(arr):
    global size
    f = open("output.txt", "w")
    for i in range(0, size):
        for j in range(0, size):
            if(len(arr[i][j])==1):
                f.write(str(arr[i][j][0]))
                f.write("\t")
            else:
                f.write("'" + str(len(arr[i][j])))
                f.write("\t")
        f.write("\n")
    f.close()


def fill(arr):
    global size
    global possible_values
    for i in range(0, size):
        for j in range(0, size):
            arr[i][j] = deepcopy(list(possible_values))


def deadlock():
    global arr
    fout(arr)
    print("deadlock")
    exit()


def done(arr):
    print("done")
    fout(arr)
    exit()


def check_rules(a, value, state, indx, indy):
    global arr
    x = not (len(a)==1)
    b = []
    for i in a:
        try:
            rules.index((i, value, state))
            b.append(i)
        except:
            pass
    arr[indx][indy] = b
    if len(b) == 1:
        return x
    if len(b) == 0:
        deadlock()
    return False


def find_by_intr(arr):
    global size
    global num
    min = 1000
    a = []
    for i in range(0, size):
        for j in range(0, size):
            if(len(arr[i][j])<min and len(arr[i][j])>1):
                a = [(i, j)]
                min = len(arr[i][j])
            elif(len(arr[i][j])==min and len(arr[i][j])>1):
                a.append((i, j))
    if num <= 0:
        done(arr)
    x = random.randint(0, len(a)-1)
    y = random.randint(0, len(arr[a[x][0]][a[x][1]])-1)
    return (a[x][0], a[x][1], arr[a[x][0]][a[x][1]][y])


def collapse(arr, b):
    global size
    global num
    num -= 1
    if(num<0):
        done(arr)
    q = []
    value = b[2]
    indx = b[0]
    indy = b[1]
    arr[indx][indy] = [value]
    if(indx+1<size):
        if check_rules(arr[indx+1][indy], value, "down", indx+1, indy):
            q.append((indx+1, indy, arr[indx+1][indy][0]))
    if(indy+1<size):
        if check_rules(arr[indx][indy+1], value, "right", indx, indy+1):
            q.append((indx, indy + 1, arr[indx][indy+1][0]))
    if (indx - 1 >= 0):
        if check_rules(arr[indx - 1][indy], value, "up", indx-1, indy):
            q.append((indx - 1, indy, arr[indx - 1][indy][0]))
    if (indy - 1 >= 0):
        if check_rules(arr[indx][indy - 1], value, "left", indx, indy-1):
            q.append((indx, indy - 1, arr[indx][indy - 1][0]))
    return q


def set_init(rul, pos):
    global rules
    global possible_values
    rules = rul
    possible_values = pos


def main():
    global arr
    for i in range(0, size):
        a = []
        for j in range(0, size):
            a.append(0)
        arr.append(a)
    fill(arr)
    while(True):
        b = find_by_intr(arr)
        q1 = collapse(arr, b)
        while(len(q1)>0):
            q2 = collapse(arr, q1[0])
            q1.remove(q1[0])
            q1 += q2




