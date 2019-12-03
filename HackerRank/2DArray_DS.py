import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):

    # ALGO:
    # start on row 2 column 2
    # calculate the hourglass here, then move column forward 1
    # repeat until second last column, start next row, row until second last one
    # Basically, I follow the middle of the hourglass and calc sum as I go

    hourglassSum = 0

    # -65 is the least possible sum (all nums -9)
    maxHourglassSum = -65

    # iterate rows, i = rows, j = cols
    for i in range(1, len(arr)-2):
        # iterate cols
        for j in range(1, len(arr)-2):
            # calculate sum
            hourglassSum = arr[i][j] + arr[i+1][j+1] + arr[i+1][j] + \
                arr[i+1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i-1][j-1]
            print(hourglassSum)
            if hourglassSum > maxHourglassSum:
                maxHourglassSum = hourglassSum

    return maxHourglassSum
