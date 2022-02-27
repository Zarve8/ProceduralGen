import random
from copy import deepcopy
import time



def lout(sout):
    print("\n\n")
    for i in range(0, 9):
        for j in range(0, 9):
            if(type(sout[i][j])==type(0)):
                print(str(sout[i][j]), end="")
            else:
                if(len(sout[i][j])==0):
                    print("*", end="")
                elif(len(sout[i][j])==1):
                    print("="+str(sout[i][j][0]), end="")
                else:
                    print("'"+str(len(sout[i][j])), end="")
            print("\t", end="")
        print("\n", end="")
    print("\n\n")


#write out file in output
def fout(sout):
    f = open("output.txt", "w")
    for i in range(0, 9):
        if (i)%3==0:
            f.write("\n")
        for j in range(0, 9):
            if (j%3) == 0:
                f.write("\t")
            if(type(sout[i][j])==type(0)):
                f.write(str(sout[i][j]))
            else:
                if(len(sout[i][j])==0):
                    f.write("*")
                elif(len(sout[i][j])==1):
                    f.write(str(sout[i][j][0]))
                else:
                    f.write("'"+str(len(sout[i][j])))
            f.write("\t")
        f.write("\n")
    f.close()


prepos = [] #list after appliying cillapse of input values
#escape process if there is and disorder
def deadlock(pos):
    global prepos
    print("deadlock")
    exit()
    return


#choose random block with smallest intropia
def choose_by_intr(pos):
    arr = []
    min = 10000
    for i in range(0, 9):
        for j in range(0, 9):
            if(type(pos[i][j])!=type(0)):
                if (len(pos[i][j]) == 0):
                    deadlock(pos)
                    return choose_by_intr(pos)
                if (len(pos[i][j]) < min):
                    min = len(pos[i][j])
                    arr.clear()
                    arr.append([i, j])
                elif (len(pos[i][j]) == min):
                    arr.append([i, j])
    x = random.randint(0, len(arr)-1)
    y = random.randint(0, len(pos[arr[x][0]][arr[x][1]])-1)
    return [arr[x][0], arr[x][1], pos[arr[x][0]][arr[x][1]][y]]


#erase posible value if it exists
def erase(pos, x, y, v):
    if (type(pos[x][y]) != type(0)):
        try:
            pos[x][y].remove(v)
        except:
            pass


#collapse list
def collapse(b, pos, num_usd):
    pos[b[0]][b[1]] = b[2]
    q = []
    for i in range(0, 9):
        erase(pos, i, b[1], b[2])
        erase(pos, b[0], i, b[2])
    x = int(b[0]/3)*3+1
    y = int(b[1]/3)*3+1
    erase(pos, x-1, y-1, b[2])
    erase(pos, x-1, y, b[2])
    erase(pos, x, y+1, b[2])
    erase(pos, x, y-1, b[2])
    erase(pos, x, y, b[2])
    erase(pos, x, y+1, b[2])
    erase(pos, x+1, y-1, b[2])
    erase(pos, x+1, y, b[2])
    erase(pos, x+1, y+1, b[2])
    num_usd[0] += 1
    return q


#set data from the input
def initialize(pos):
    # open file with input array
    fin = open("input.txt", "r")
    rows = fin.read().splitlines()
    siin = []
    for i in rows:
        a = [int(j) for j in i.split()]
        siin.append(a)
    # initialize array from input data
    q = []
    for i in range(0, 9):
        a = []
        for j in range(0, 9):
            if (siin[i][j] == 0):
                a.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
            else:
                a.append([siin[i][j]])
                q.append([i, j, siin[i][j]])
        pos.append(a)
    return q


#cycle task until all blocks set or there is an dead end
num_usd = [0]
pos = []
q = initialize(pos)
while(len(q)>0 and num_usd[0]<-1):
        q2 = collapse(q[0], pos, num_usd)
        lout(pos)
        q.remove(q[0])
        q += q2
prepos = pos
while(num_usd[0]<81):
    b = choose_by_intr(pos)
    q = collapse(b, pos, num_usd)
fout(pos)


