class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == "":
            return True

        # parsedS = ''.join(char for char in s if char.isalnum()).lower()

        # # 2 ways to do it

        # if parsedS == '':
        #     return True
        # print(parsedS[::-1])
        # return parsedS == parsedS[::-1]
        l = 0
        r = len(s)-1
        while l < r:
            while (not s[l].isalnum() and l < r):
                l += 1
            while (not s[r].isalnum() and r > l):
                r -= 1
            print("left: " + s[l] + " right:" + s[r])
            print(l, r)
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


sln = Solution()
ans1 = sln.isPalindrome("race !*' car _")
# ans2 = sln.isPalindrome("A man, a plan, a canal: Panama")
# ans3 = sln.isPalindrome("!^@&a*#(")
ans4 = sln.isPalindrome(
    "Nella's simple hymn: \"I attain my help, Miss Allen.\"")
print(ans1)
