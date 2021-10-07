class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0 for i in range(len(text1) + 1)]
              for j in range(len(text2) + 1)]

        # for row in dp:
        #     print(row)
        text1 = " " + text1
        text2 = " " + text2
        # print("\nnew:\n")
        for rowNum in range(1, len(text2)):
            for colNum in range(1, len(text1)):
                if text1[colNum] == text2[rowNum]:
                    dp[rowNum][colNum] = 1 + dp[rowNum - 1][colNum - 1]
                    # print("same: ", rowNum, colNum, dp[rowNum][colNum])
                else:
                    dp[rowNum][colNum] = max(
                        dp[rowNum - 1][colNum], dp[rowNum][colNum - 1])
                    # print("diff: ", rowNum, colNum, dp[rowNum][colNum])

        # for row in dp:
        #     print(row)

        return dp[len(text2) - 1][len(text1) - 1]


obj = Solution()
ans = obj.longestCommonSubsequence("fsgdf", "fgzsde")
print(ans)
