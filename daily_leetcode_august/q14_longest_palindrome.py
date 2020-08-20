class Solution:
    def longestPalindrome(self, s: str) -> int:
        charDict = {}
        for char in s:
            charDict[char] = charDict.get(char, 0) + 1

        print(charDict)
        palLen = 0
        addedCenter = False
        for val in charDict.values():
            if val % 2 == 0:
                palLen += val
            elif addedCenter == False:
                palLen += val
                addedCenter = True
            elif val > 1:
                palLen += val - 1
        return palLen

        # charDict = {}
        # for char in s:
        #     if char in charDict:
        #         charDict[char] += 1
        #     else:
        #         charDict[char] = 1

        # leftPal = ""
        # rightPal = ""

        # for key in charDict.keys():
        #     if charDict[key] % 2 == 0:
        #         charCount = charDict[key]
        #         evenString = key * int(charCount / 2)
        #         leftPal = evenString + leftPal
        #         rightPal = rightPal + evenString

        # oddCharList = list(filter(lambda count: count %
        #                           2 == 1, charDict.values()))
        # print(oddCharList)
        # if oddCharList:
        #     maxOddCharCount = max(oddCharList)
        #     for char in charDict:
        #         if charDict[char] == maxOddCharCount:
        #             maxOddChar = char
        #             break
        #     leftPal = (maxOddChar * int((maxOddCharCount-1)/2)) + \
        #         leftPal + maxOddChar
        #     rightPal = rightPal + (maxOddChar * int((maxOddCharCount-1)/2))

        # fullPal = leftPal + rightPal
        # print(fullPal)
        # return len(fullPal)


x = Solution()
ans = x.longestPalindrome("aAAcccccccbddd")
print(ans)
