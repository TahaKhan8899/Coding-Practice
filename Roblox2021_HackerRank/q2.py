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
    # go through all chars in word
    for i in range(0, len(word)):
        # if we havent seen it, add char and freq=1 to the stack
        if len(stk) == 0:
            charFreq = [word[i], 1]
            stk.append(charFreq)
            continue
        # is the top of the stack the same as the current char?
        if stk[len(stk)-1][0] == word[i]:
            # increase freq of that char in the stack
            stk[len(stk)-1][1] += 1
            # is that new freq == k?
            if stk[len(stk)-1][1] == k:
                stk.pop()
        else:
            # char not on top of stack, add the char and freq=1 to stack
            charFreq = [word[i], 1]
            stk.append(charFreq)

    # construct the final string using what is left on the stack
    finalWord = ""
    for i in range(0, len(stk)):
        subString = stk[i][0] * stk[i][1]
        finalWord += subString

    return finalWord


# print(maxEvents([1, 3, 3, 5, 7], [2, 2, 1, 2, 1]))
# print(maxEvents([1, 3, 5], [2, 2, 2]))
print(maxEvents([1], [1]))
