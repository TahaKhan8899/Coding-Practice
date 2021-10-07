#
# Complete the 'compressWord' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING word
#  2. INTEGER k
#

def compressWord(word, k):
    stk = []
    for i in range(0, len(word)):
        if len(stk) == 0:
            charFreq = [word[i], 1]
            stk.append(charFreq)
            print(stk)
            continue
        print(stk)
        if stk[len(stk)-1][0] == word[i]:
            stk[len(stk)-1][1] += 1
            if stk[len(stk)-1][1] == k:
                stk.pop()
        else:
            charFreq = [word[i], 1]
            stk.append(charFreq)
        print(stk)

    finalWord = ""
    subString = ""
    for i in range(0, len(stk)):
        subString = stk[i][0] * stk[i][1]
        finalWord += subString
        print(finalWord)

    return finalWord


print(compressWord("aba", 2))
