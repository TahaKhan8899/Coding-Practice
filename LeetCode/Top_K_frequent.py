from MaxHeap import MaxHeap 

class Solution:
    def topKFrequent(self, words, k):

        wordCount = {}

        for i in range(len(words)):

            word = words[i]
            if wordCount.get(word):
                wordCount[word] += 1
            else:
                wordCount[word] = 1
        
        print("Dict: ", wordCount)

        wordHeap = MaxHeap(set(wordCount.values()))
        finalSortedMaxWords = []

        while k > 0:

            if len(wordHeap.heap) > 1:
                maxWordOccurences = wordHeap.pop()
            else:
                break
            # print(maxWordOccurences)

            wordssss = findValue(wordCount, maxWordOccurences)

            wordsz = sorted(wordssss)
            print("LENNNN: ", len(wordsz), " ", wordsz)
            
            if len(wordsz) <= k:
                for word in wordsz:
                    finalSortedMaxWords.append(word)
            else:
                i = 0
                while k > 0 and i < len(wordsz):
                    word = wordsz[i]
                    finalSortedMaxWords.append(word)
                    k -= 1
                    i += 1
                k = 0
        
            k -= len(wordsz)
            
        return finalSortedMaxWords


def findValue(wordCount, maxWordOccurences):

    listOfMaxWords = []

    for key, occurence in wordCount.items():   
        if maxWordOccurences == occurence:
            listOfMaxWords.append(key)
    
    print("MAXYYYY: ", listOfMaxWords)

    return listOfMaxWords


sol = Solution()
words1 = ["zzzzzeee", "ok", "hi", "zzzzzeee", "ok"]
words2 = ["i", "love", "leetcode", "i", "love", "leetcode", "i"]
k = 3
print(sol.topKFrequent(words2, k))

        