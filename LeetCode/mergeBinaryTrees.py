# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def appendNode(self, node):
        self.left = node


class Solution:

    gayTree = TreeNode(None)
    gayTree.mergeTrees(t1, t2)

    def mergeTrees(self, t1, t2):
        newTree = TreeNode(None)

        if t1 is not None and t2 is not None:
            newTree = TreeNode(t1.val + t2.val)
            self.appendNode(newTree)
            self.mergeTrees(t1.left, t2.left)
            self.mergeTrees(t1.right, t2.right)

        traverseTreePreOrder(gayTree)


def traverseTreePreOrder(root):
    if root is not None:
        print(root.val)
        traverseTreePreOrder(root.left)
        traverseTreePreOrder(root.right)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.left = n2
n1.right = n3

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)

t1.left = t2
t1.right = t3

# traverseTreePreOrder(n1)
obj = Solution()
obj.mergeTrees(n1, t1)
