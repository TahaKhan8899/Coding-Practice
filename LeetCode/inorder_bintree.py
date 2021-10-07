# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        output = []
        if not root:
            return output
        return traversalHelper(root, output)


def traversalHelper(node, output):
    if node.left:
        traversalHelper(node.left, output)
    output.append(node.val)
    print(output)
    if node.right:
        traversalHelper(node.right, output)
    return output


#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
#  /
# 10
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(10)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(8)

ans = Solution().inorderTraversal(root)
