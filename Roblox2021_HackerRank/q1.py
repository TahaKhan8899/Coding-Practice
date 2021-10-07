#
# Complete the 'slowestKey' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts 2D_INTEGER_ARRAY keyTimes as parameter.
#

def slowestKey(keyTimes):
    currentTime = 0
    longestTime = 0
    chars = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm',
             13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
    for i in range(0, len(keyTimes)):
        if i == 0:
            currentTime = keyTimes[i][1] - 0
        else:
            currentTime = keyTimes[i][1] - keyTimes[i-1][1]
        print("curr: ", currentTime)
        if currentTime > longestTime:
            longestTime = currentTime
            keyWithLongest = keyTimes[i][0]
        print("longest: ", longestTime)
        print(keyWithLongest)

    return chars[keyWithLongest]


print(slowestKey([[0, 2], [1, 5], [0, 9], [2, 15]]))
