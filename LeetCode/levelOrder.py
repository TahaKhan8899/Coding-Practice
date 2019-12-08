# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):

        allRows = []
        if root:
            que = [root]
        else:
            return allRows

        while que:
            lenOfRow = len(que)
            oneRow = []
            for _ in range(0, lenOfRow):
                node = que.pop(0)
                oneRow.append(node.val)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            print("One Row: ", oneRow)
            allRows.append(oneRow)
            oneRow = []

        return allRows


root = None
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
obj = Solution()
ans = obj.levelOrder(root)
print(ans)
