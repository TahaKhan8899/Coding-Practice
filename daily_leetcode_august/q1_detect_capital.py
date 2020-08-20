class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        wordCopyUpper = word.upper()
        wordCopyLower = word.lower()
        wordCopyStartCaps = word[0].upper() + word[1:].lower()
        validOptions = [wordCopyUpper, wordCopyLower, wordCopyStartCaps]
        print(validOptions)

        if word in validOptions:
            return True

        return False


sln = Solution()
answer = sln.detectCapitalUse("UsA")
print(answer)
