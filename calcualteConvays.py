import numpy
import os
import time
import imageio.v2 as iio



img = iio.imread("./map.png")
iio.imwrite("./map.png",img)

print (img[0,0])

mapXsize = img.shape[0]
mapYsize = img.shape[1]
map = numpy.ones((mapXsize,mapYsize))
for x in range(0,mapXsize):
    for y in range(0,mapYsize):
        map[x,y] = 1 if img[x,y,0] == 0 else 0

def neighboursCount(x,y):
    indexX = 0
    indexY = 0
    count = 0
    #U
    indexX = x
    indexY = y-1
    if 0 <= indexX < mapXsize and 0 <= indexY < mapYsize:
        if map[indexX,indexY] != 0:
            count += 1
    #D
    indexX = x
    indexY = y+1
    if 0 <= indexX < mapXsize and 0 <= indexY < mapYsize:
        if map[indexX,indexY] != 0:
            count += 1
    #R
    indexX = x+1
    indexY = y
    if 0 <= indexX < mapXsize and 0 <= indexY < mapYsize:
        if map[indexX,indexY] != 0:
            count += 1
    #L
    indexX = x-1
    indexY = y
    if 0 <= indexX < mapXsize and 0 <= indexY < mapYsize:
        if map[indexX,indexY] != 0:
            count += 1
    #UR
    indexX = x+1
    indexY = y-1
    if 0 <= indexX < mapXsize and 0 <= indexY < mapYsize:
        if map[indexX,indexY] != 0:
            count += 1
    #UL
    indexX = x-1
    indexY = y-1
    if 0 <= indexX < mapXsize and 0 <= indexY < mapYsize:
        if map[indexX,indexY] != 0:
            count += 1
    #DR
    indexX = x+1
    indexY = y+1
    if 0 <= indexX < mapXsize and 0 <= indexY < mapYsize:
        if map[indexX,indexY] != 0:
            count += 1
    #DL
    indexX = x-1
    indexY = y+1
    if 0 <= indexX < mapXsize and 0 <= indexY < mapYsize:
        if map[indexX,indexY] != 0:
            count += 1
    
    return count
    


def nextGeneration(map):
    nexG = numpy.zeros((mapXsize,mapYsize))
    for x in range(0,mapXsize):
        for y in range(0,mapYsize):
            neighbours = neighboursCount(x,y)
            next = 0
            if map[x,y] == 0:
                if neighbours == 3:
                    next = 1
            else:
                if 2 <= neighbours <=3:
                    next = 1
            nexG[x,y] = next
    return nexG

 


def printArray(arr):
    output = ""
    for i in arr:
        for j in i:
            output += " 1 " if j != 0 else "   "
        output += "\n"
    print (output)
    


        
#Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by overpopulation.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction







while True:
    printArray(map)
    time.sleep(0.1)
    os.system('cls')
    map = nextGeneration(map)