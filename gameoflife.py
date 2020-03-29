from threading import Thread
from numpy import zeros
from random import randrange
from matplotlib import pyplot as plot
from matplotlib import animation

width, height = 800, 400
dotres = 20

col = int(width/dotres)
row = int(height/dotres)

def defineArray(row, col):
    array = zeros((row, col))
    for x in range(row):
        for y in range(col):
            array[x][y] = randrange(0,2)
    return array

def neighbourCellCounter(array, xo, yo):
    # xo, yo - center cell position
    # Go around the neighbour cells
    # Count the alive ones

    aliveSum = 0
    for x in range(0,2):
        for y in range(0,2):
            print (xo + x, yo + y)
            aliveSum += array[xo + x][yo + y]
    aliveSum -= array[xo][yo]
    return aliveSum

def updateGrid(i):
    # Create a new grid system based on the last one
    nextScene = defineArray(row, col)
    for x in range(row):
        for y in range(col):
            cellState = ogScene[x][y]
            if x == 0 or x == col - 1 or y == 0 or y == row - 1:
                nextScene[x][y] = cellState
                break
            else:
                nSum = neighbourCellCounter(ogScene, x, y)
                if cellState == 0 and nSum == 3:
                    nextScene[x][y] = 1
                elif cellState == 1 and (nSum < 2 or nSum > 3):
                    nextScene[x][y] = ogScene[x][y]
    ax.imshow(nextScene)

# Neighbour cells system
# 1 2 3
# 4 o 6
# 7 8 9
#
# 1 -> array[x - 1][y - 1]
# 2 -> array[x - 1][y]
# 3 -> array[x - 1][y + 1]
# 4 -> array[x][y - 1]
# 6 -> array[x][y + 1]
# 7 -> array[x + 1][y - 1]
# 8 -> array[x + 1][y]
# 8 -> array[x + 1][y + 1]


# Elements are referenced [row][column] with starting index 0
ogScene = defineArray(row, col)
#plot.imshow(ogScene, interpolation='nearest')

fig, ax = plot.subplots()
matrice = ax.matshow(ogScene)
plot.gray()

#
ani = animation.FuncAnimation(fig, updateGrid, frames=60, interval=50)
plot.show()
