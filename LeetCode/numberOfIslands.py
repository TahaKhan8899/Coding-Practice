class Solution:
    def numIslands(self, grid):
        # starting at the top left, find all adjacent islands using a helper function and mark them with a 2 if visited
        # increase island count by 1
        # find the next unmarked island and repeat the same helper function

        if len(grid[0]) < 1:
            return 0
        islandCount = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                currentPos = (row, col)
                # print("currentPos: ", currentPos)
                printGrid(grid)
                if grid[row][col] == '1':
                    grid = markAdjIslands(currentPos, grid)
                    islandCount += 1

        return islandCount


def markAdjIslands(currentPos, grid):
    stack = [currentPos]
    rowLen = len(grid)
    colLen = len(grid[0])
    # print("grid before: ")
    # printGrid(grid)
    while stack:
        currentPos = stack.pop(len(stack)-1)
        currentRow = currentPos[0]
        currentCol = currentPos[1]
        # mark it as visited
        # print("current pos: ", currentPos)
        # print("current grid: ")
        # printGrid(grid)
        grid[currentRow][currentCol] = '2'

        # check right
        if currentCol < colLen - 1:
            if grid[currentRow][currentCol + 1] == '1':
                grid[currentRow][currentCol + 1] = '1*'
                stack.append((currentRow, currentCol + 1))

        # check bottom
        if currentRow < rowLen - 1:
            if grid[currentRow + 1][currentCol] == '1':
                grid[currentRow + 1][currentCol] = '1*'
                stack.append((currentRow + 1, currentCol))

        # check left
        if currentCol > 0:
            if grid[currentRow][currentCol - 1] == '1':
                grid[currentRow][currentCol - 1] = '1*'
                stack.append((currentRow, currentCol - 1))

        # check up
        if currentRow > 0:
            if grid[currentRow - 1][currentCol] == '1':
                grid[currentRow - 1][currentCol] = '1*'
                stack.append((currentRow - 1, currentCol))
        # print("stack: ", stack)
    # print("grid after: ")
    # printGrid(grid)
    return grid


def printGrid(grid):
    for row in grid:
        print(row)


grid1 = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
# grid1 = [["1", "1", "1", "1"], ["0", "1", "1", "1"],
#          ["1", "0", "1", "1"], ["1", "1", "1", "1"]]
# grid1 = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]
ans = Solution().numIslands(grid1)
print(ans)
