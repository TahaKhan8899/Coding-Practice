class Solution:
    def findRepeatedDnaSequences(self, s):
        output = []
        if len(s) <= 10:
            return output

        substringMap = {}

        left = 0
        right = 9
        print(len(s))
        while right <= len(s) - 1:
            print(right)
            subString = s[left:right+1]
            print(subString)
            if subString in substringMap:
                substringMap[subString] += 1
            else:
                substringMap[subString] = 1
            left += 1
            right += 1

        for key in substringMap:
            if substringMap[key] >= 2:
                output.append(key)

        return output


ans = Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print(ans)
