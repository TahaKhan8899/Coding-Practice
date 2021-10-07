# Complete the rotLeft function below.
def rotLeft(a, d):
    newArr = [0 for i in range(len(a))]
    for i in range(0, len(a)):
        newInd = i - d
        newArr[newInd] = a[i]

    return newArr

print(rotLeft([1,2,3,4,5,6], 3))
