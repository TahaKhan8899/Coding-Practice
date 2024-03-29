def maxFreq(s, maxLetters, minSize, maxSize):

    validWords = {}
    for i in range(0, len(s)):
        for j in range(i + minSize - 1, min(i + maxSize, len(s))):
            ss = s[i:j + 1]
            if len(set(ss)) <= maxLetters:
                if ss in validWords:
                    validWords[ss] += 1
                else:
                    validWords[ss] = 1

    print("valid: ", validWords)
    if validWords:
        all_values = validWords.values()
        return max(all_values)
    else:
        return 0


print(maxFreq("aababcaab", 2, 3, 4))
