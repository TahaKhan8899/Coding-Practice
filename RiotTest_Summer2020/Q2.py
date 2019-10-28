#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the 'PrintGardenLayoutWithIdealSeats' function below.

def PrintGardenLayoutWithIdealSeats():
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
    
    hasFlowers = False
    # map garden
    for pair in data:

        t = pair[0]

        # check if garden has a flower
        if not hasFlowers:
            if t == "F":
                hasFlowers = True

        row = int(pair[2])
        col = int(pair[1])

        garden[row][col] = t

    # replace 0s with 'B's
    textLayout = ""
    for i in range(len(garden)):
        oneGarden = garden[i]

        for j in range(len(oneGarden)):

            if oneGarden[j] == 0:
                # handle edge case of no flowers
                if not hasFlowers:
                    garden[i][j] = "*"
                else:
                    garden[i][j] = "B"
            
            textLayout += garden[i][j]
        textLayout += '\n'
        
    # print(textLayout)

    findBestLocation(garden, w, h)

def findBestLocation(garden, w, h):
    # print("Finding FLowers: ", garden)

    maxNumFlowers = 0

    # generate empoty mapOfFlowerCounts
    mapOfFlowerCounts = [[0 for j in range(w)] for i in range(h)]

    for i in range(len(garden)):
        oneGarden = garden[i]

        for j in range(len(oneGarden)):

            totalFlowerCount = countFlowers(garden, i, j, mapOfFlowerCounts)
            # print("MAP: ", mapOfFlowerCounts)

            if totalFlowerCount > maxNumFlowers:
                maxNumFlowers = totalFlowerCount
    # print("max: ", maxNumFlowers)

    markedGarden = markSpots(garden, maxNumFlowers, mapOfFlowerCounts)
    printGarden(markedGarden)

def printGarden(garden):
    textLayout = ""
    for i in range(len(garden)):
        oneGarden = garden[i]

        for j in range(len(oneGarden)):
            
            textLayout += garden[i][j]
        textLayout += '\n'
    
    print(textLayout)

def markSpots(garden, maxNumFlowers, mapOfFlowerCounts):

    for i in range(len(garden)):
        oneGarden = garden[i]

        for j in range(len(oneGarden)):

            if mapOfFlowerCounts[i][j] == maxNumFlowers:
                garden[i][j] = "*"

    return garden

def countFlowers(garden, i, j, mapOfFlowerCounts):
    totalFlowerCount = checkNorth(garden, i, j)
    totalFlowerCount += checkSouth(garden, i, j)
    totalFlowerCount += checkEast(garden, i, j)
    totalFlowerCount += checkWest(garden, i, j)
    mapOfFlowerCounts[i][j] = totalFlowerCount

    # print("My position is: ", i, " ", j, ". TOTAL Flower Count is: ", totalFlowerCount)
    return totalFlowerCount

def checkWest(garden, i, j):
    colPos = j
    flowerCount = 0
    while colPos > 0:
        lookingAt = garden[i][colPos-1]
        if lookingAt == "W":
            break
        elif lookingAt == "F":
            flowerCount += 1
        colPos -= 1
    
    return flowerCount

def checkEast(garden, i, j):
    
    colPos = j
    flowerCount = 0
    while colPos < len(garden[i])-1:
        lookingAt = garden[i][colPos+1]
        if lookingAt == "W":
            break
        elif lookingAt == "F":
            flowerCount += 1
        colPos += 1
    
    return flowerCount

def checkSouth(garden, i, j):

    rowPos = i
    flowerCount = 0
    while rowPos < len(garden)-1:
        lookingAt = garden[rowPos+1][j]
        if lookingAt == "W":
            break
        elif lookingAt == "F":
            flowerCount += 1
        rowPos += 1
    
    return flowerCount

def checkNorth(garden, i, j):

    rowPos = i
    flowerCount = 0
    while rowPos > 0:
        lookingAt = garden[rowPos-1][j]
        if lookingAt == "W":
            break
        elif lookingAt == "F":
            flowerCount += 1
        rowPos -= 1
        
    return flowerCount
    

if __name__ == '__main__':