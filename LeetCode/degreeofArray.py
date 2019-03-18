import operator
from collections import OrderedDict

def degreeOfArray(arr):

    dict = OrderedDict()
    subarray = []

    #go through string and add count for each char in a dict
    for i in range(0, len(arr)):
        if arr[i] in dict:
            dict[arr[i]] += 1
        else:
            dict[arr[i]] = 1

    maxLetter = arr[0]

    #find element with max count
    for key in dict:
        if dict[key] >= dict[maxLetter]:
            maxLetter = key

    subarray.append(maxLetter)

    for key in dict:
        if dict[key] == dict[maxLetter] and key != maxLetter:
            subarray.append(key)

    print(maxLetter)
    print(subarray)

    return(dict[maxLetter])

print(degreeOfArray([1,2,2,3,1]))
