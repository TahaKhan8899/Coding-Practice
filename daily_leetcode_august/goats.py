class Solution:
    def toGoatLatin(self, S: str) -> str:
        finalSentence = ""
        vowels = "aeiouAEIOU"
        words = S.split()

        for i in range(0, len(words)):
            if words[i][0] in vowels:
                finalSentence += words[i] + "ma" + ('a' * (i + 1)) + " "
            else:
                finalSentence += words[i][1:] + words[i][0] + \
                    "ma" + ('a' * (i + 1)) + " "

        return finalSentence


obj = Solution()
answer = obj.toGoatLatin("The quick brown fox jumped over the lazy dog")
print(answer)
