# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumRootToLeaf(self, root: TreeNode) -> int:
        paths = []
        if not root:
            return None

        preOrder(root, "", paths)
        totalSum = 0
        for path in paths:
            baseTen = 0
            exp = 0
            for digit in path[::-1]:
                baseTen += int(digit) * (2 ** exp)
                exp += 1
            totalSum += baseTen
        return totalSum


def preOrder(node, currPath, paths):
    currPath += str(node.val)
    if not node.left and not node.right:
        paths.append(currPath)
        return
    if node.left:
        preOrder(node.left, currPath, paths)
    if node.right:
        preOrder(node.right, currPath, paths)


root = TreeNode(1, None, None)

root.right = TreeNode(1)
root.right.right = TreeNode(1)
root.right.left = TreeNode(0)

root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)

ans = Solution().sumRootToLeaf(root)
print(ans)
