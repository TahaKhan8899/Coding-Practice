from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        # algorithm:
        # first: linear traversal and find the first island
        # then: BFS to find adjacent cells
        # update perimeter
        # For BFS, add adjacent land cells to queue
        # while queue is not empty:
        # dequeue, go to that land cell,
        # keep track of perimeter based on how many
        # water cells surround a land cell
        # enqueue any adjacent land cells
        # repeat loop

        # Now go through list of land cells to calculate perimeter
        # based on how many water cells are around it

        firstLandCords = {}

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    firstLandCords['row'] = r
                    firstLandCords['col'] = c
                    break

            if len(firstLandCords) > 0:
                break

        queue = []
        # print("first cords: ", firstLandCords)
        # calculate init perimeter
        firstRow = firstLandCords['row']
        firstCol = firstLandCords['col']
        grid[firstRow][firstCol] = 2
        perim, queue, grid = self.examineAdjCells(self,
                                                  firstLandCords, grid, queue)
        # print("init perim = ", perim)
        # print("updated queue = ", queue)

        while (len(queue) > 0):
            currentLocation = queue.pop()
            # print("now visiting: ", currentLocation)
            adjWater, queue, grid = self.examineAdjCells(self,
                                                         currentLocation, grid, queue)
            perim += adjWater
            # print("new perim = ", perim)
            # print("updated queue = ", queue)

        return perim

    def examineAdjCells(self, landCord, grid, queue):
        row = landCord['row']
        col = landCord['col']

        numWaterCells = 0

        # check top
        if (row == 0):
            numWaterCells += 1
        else:
            if (grid[row-1][col] == 0):
                numWaterCells += 1
            elif (grid[row-1][col] == 1):
                newCell = {'row': row-1, 'col': col}
                queue = [newCell] + queue
                grid[row-1][col] = 2

        # check right
        if (col == len(grid[0])-1):
            numWaterCells += 1
        else:
            if (grid[row][col+1] == 0):
                numWaterCells += 1
            elif (grid[row][col+1] == 1):
                newCell = {'row': row, 'col': col+1}
                queue = [newCell] + queue
                grid[row][col+1] = 2

        # check left
        if (col == 0):
            numWaterCells += 1
        else:
            if (grid[row][col-1] == 0):
                numWaterCells += 1
            elif (grid[row][col-1] == 1):
                newCell = {'row': row, 'col': col-1}
                queue = [newCell] + queue
                grid[row][col-1] = 2

        # check bottom
        if (row == len(grid)-1):
            numWaterCells += 1
        else:
            if (grid[row+1][col] == 0):
                numWaterCells += 1
            elif (grid[row+1][col] == 1):
                newCell = {'row': row+1, 'col': col}
                queue = [newCell] + queue
                grid[row+1][col] = 2

        # print("grid:")
        # for row in grid:
        #     print(row)

        return numWaterCells, queue, grid


obj = Solution
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
ans = obj.islandPerimeter(obj, grid)

print("ans = ", ans)
