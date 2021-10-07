class Solution:
    def longestCommonPrefix(self, strs):

        commonPrefix = ""
        if not strs:
            return commonPrefix

        commonPrefix = strs[0]
        print(commonPrefix)
        for word in strs[1:]:
            if not word:
                return ""
            commonPrefix = unionStrings(commonPrefix, word)
            print(commonPrefix)

        return commonPrefix


def unionStrings(s1, s2):
    common = ""
    print("unioning " + s1 + " and " + s2)
    for i in range(len(s1)):
        print(i)
        if i > len(s2)-1:
            break
        if s1[i] == s2[i]:
            common += s1[i]
        else:
            break
    return common


strs1 = ["flow", "flower", "flight"]
strs2 = ["dog", "dong", "donut"]
ans = Solution().longestCommonPrefix(strs2)
print("ans is: " + ans)
