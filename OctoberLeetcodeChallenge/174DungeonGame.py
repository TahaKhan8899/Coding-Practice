from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        print("dungeon:")
        for row in dungeon:
            print(row)
        rowNums = len(dungeon)
        colNums = len(dungeon[0])
        rInd = rowNums - 1
        cInd = colNums - 1

        dp = [[-10**9 for i in range(colNums)] for j in range(rowNums)]

        if (dungeon[rInd][cInd] < 0):
            dp[rInd][cInd] = abs(dungeon[rInd][cInd]) + 1
        else:
            dp[rInd][cInd] = 1

        # Fill out right column
        for r in range(rInd-1, -1, -1):
            print('running')
            if dungeon[r][cInd] < 0:
                dp[r][cInd] = abs(dungeon[r][cInd]) + dp[r + 1][cInd]
            else:
                dp[r][cInd] = max(1, dp[r + 1][cInd] - dungeon[r][cInd])

        # Fill out bottom row
        for c in range(cInd-1, -1, -1):
            print("yee")
            if dungeon[rInd][c] < 0:
                dp[rInd][c] = abs(dungeon[rInd][c]) + dp[rInd][c + 1]
            else:
                dp[rInd][c] = max(1, dp[rInd][c + 1] - dungeon[rInd][c])

        # fill out inside cells
        for r in range(rInd-1, -1, -1):
            for c in range(cInd-1, -1, -1):
                if dungeon[r][c] < 0:
                    dp[r][c] = abs(dungeon[r][c]) + \
                        min(dp[r+1][c], dp[r][c+1])
                else:
                    dp[r][c] = max(
                        min(dp[r+1][c], dp[r][c+1]) - dungeon[r][c], 1)

        print("dp:")
        for row in dp:
            print(row)

        return dp[0][0]


obj = Solution
ans = obj.calculateMinimumHP(obj, dungeon=[[3, -20, 30], [-3, 4, 0]])
print(ans)
