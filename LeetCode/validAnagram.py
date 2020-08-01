def isAnagram(s, t):

    if len(s) == 0 or len(t) == 0:
        return False

    dictS = createDict(s)
    dictT = createDict(t)

    print(dictS)
    print(dictT)

    isValid = True
    for i in dictS:
        print(i)
        if i not in dictT:
            print("Not in it")
            isValid = False
            break
        if dictS[i] != dictT[i]:
            isValid = False

    return isValid


def createDict(lst):
    newDict = {}
    for i in range(len(lst)):
        if lst[i] in newDict:
            newDict[lst[i]] += 1
        else:
            newDict[lst[i]] = 1
    return newDict


def test1():

    s = ""
    t = "car"
    print(isAnagram(s, t))


test1()
