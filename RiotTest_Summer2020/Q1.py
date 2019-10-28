#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'PrintGardenLayout' function below.
def PrintGardenLayout():

    # get width and heigth
    size = sys.stdin.readline().split(',')
    w = int(size[0])
    h = int(size[1])

    # generate empty garden
    garden = [[0 for j in range(w)] for i in range(h)]
    data = []
    for line in sys.stdin:
        inp = line.split(',')
        data.append(inp)
    
    # map garden
    for pair in data:

        t = pair[0]

        row = int(pair[2])
        col = int(pair[1])

        garden[row][col] = t

    # replace 0s with 'B's
    textLayout = ""
    for i in range(len(garden)):
        oneGarden = garden[i]

        for j in range(len(oneGarden)):

            if oneGarden[j] == 0:
                garden[i][j] = "B"
            
            textLayout += garden[i][j]
        textLayout += '\n'
        
    print(textLayout)

if __name__ == '__main__':
    PrintGardenLayout()