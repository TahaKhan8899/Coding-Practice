def lengthOfLongestSubstring(s):
    subStringDict = {}
    maxLen = 0
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    for i in range(0, len(s) - 1):
        subStringDict[s[i]] = 1
        print("outter char: ", s[i])
        for j in range(i + 1, len(s)):
            print("current dict: ", subStringDict)
            print("j: ", s[j])
            if s[j] in subStringDict or j == len(s) - 1:
                if s[j] not in subStringDict:
                    subStringDict[s[j]] = 1
                newLen = len(subStringDict)
                if newLen > maxLen:
                    maxLen = newLen
                subStringDict = {}
                print("Max is now: ", maxLen)
                break
            else:
                subStringDict[s[j]] = 1
    return maxLen


print(lengthOfLongestSubstring("pwwkew"))
