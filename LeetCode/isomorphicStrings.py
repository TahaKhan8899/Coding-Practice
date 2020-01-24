def isIsomorphic(str1, str2):

    mapStr1toStr2 = {}
    mapStr2toStr1 = {}

    for i in range(0, len(str1)):

        char1 = str1[i]
        char2 = str2[i]
        if char1 not in mapStr1toStr2:
            mapStr1toStr2[char1] = char2
            print("map1: ", mapStr1toStr2)
        else:
            if char2 != mapStr1toStr2[char1]:
                print(char1, "maps to 2 chars: ", char2,
                      " and ", mapStr1toStr2[char1])
                return False
        if char2 not in mapStr2toStr1:
            mapStr2toStr1[char2] = char1
            print("map2: ", mapStr2toStr1)
        else:
            if char1 != mapStr2toStr1[char2]:
                print(char2, "maps to 2 chars: ", char1,
                      " and ", mapStr2toStr1[char2])
                return False

    return True


str1 = "ab"
str2 = "aa"
print(isIsomorphic(str1, str2))
