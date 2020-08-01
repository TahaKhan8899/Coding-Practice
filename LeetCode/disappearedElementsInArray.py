def disappeared(arr):

    if not arr:
        return []

    numsDict = {}

    for i in range(1, len(arr)+1):
        numsDict[i] = 0

    for num in arr:
        if num in numsDict:
            numsDict[num] += 1

    missing = [k for k, v in numsDict.items() if v == 0]

    return missing


def test():

    ans = disappeared([1, 10])
    print(ans)


test()
