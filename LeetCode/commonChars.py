from collections import Counter

class Solution:
    def commonChars(self, A):

        initialDict = Counter(A[0])
        print("initialDict: ", initialDict)

        for word in A[1:]:
            thisWordCountDict = Counter(word)
            for char in initialDict:
                if char in thisWordCountDict:
                    print(word, " also contains: ", char, "with count: ", thisWordCountDict[char])
                    if thisWordCountDict[char] < initialDict[char]:
                        initialDict[char] = thisWordCountDict[char]
                        print("New value: ", initialDict)
                else:
                    initialDict[char] = 0
                    print("On", word, "Reset value: ", char, " ", initialDict)

        arrayOfCommonChars = []
        for char in initialDict:
            if initialDict[char] > 0:
                for i in range(0, initialDict[char]):
                    arrayOfCommonChars.append(char)
        print(arrayOfCommonChars)

        return arrayOfCommonChars
            

obj = Solution()
A = ["bella", "lab", "llamb"]
ans = obj.commonChars(A)
print("final answer: ", ans)
