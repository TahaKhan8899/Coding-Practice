# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        traversalOrder = []

        if root is None:
            return traversalOrder

        colItems = {}
        self.minCol, self.maxCol = 0, 0

        # do dfs and track the points I reach, point = [row#, nodeValue], in colItems
        def dfs(node, row, col):
            # empty node, go back in the traversal
            if node == None:
                return
            # check if I have visited this col before, if yes, add it to the list of points at this col#
            if col in colItems:
                colItems[col].append([row, node.val])
            else:
                # create a new list of points at this col#
                colItems[col] = [[row, node.val]]
            # have I found a new min and max col?
            self.minCol = min(self.minCol, col)
            self.maxCol = max(self.maxCol, col)

            # traverse left, then right
            dfs(node.left, row+1, col-1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        # at this point I have all colItems, which is a dict mapping col#'s to points
        # Go through the col#'s in order
        for col in range(self.minCol, self.maxCol+1):
            # sort the points at this col#
            sortedColumnItems = sorted(
                colItems[col], key=lambda item: (item[0], item[1]))
            # use this to extract only the values from the points in each col# in sortedColumnItems
            nodesInSortedOrder = []
            for point in sortedColumnItems:
                nodesInSortedOrder.append(point[1])

            # add the array of nodes for this column to the traversal order final array
            traversalOrder.append(nodesInSortedOrder)

        return traversalOrder
