class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pal = True

        lo = 0
        hi = len(s)-1

        while(lo < hi):
            if (s[lo] != s[hi]):
                pal = False
            lo += 1
            hi -= 1

        return pal

obj = Solution()
print(obj.isPalindrome("racecar"))
