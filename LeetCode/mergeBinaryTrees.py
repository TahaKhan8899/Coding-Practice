# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def appendNode(self, node):
        self.left = node


class Solution:
    def mergeTrees(self, t1, t2):

        # make new root node
        if t1 is not None and t2 is not None:
            newRoot = TreeNode(t1.val + t2.val)

            # traverse and add to new root node
            newTree = overlapTraverse(t1, t2, newRoot)
            traverseTreePreOrder(newTree)
        else:
            return None


def overlapTraverse(t1, t2, newTree):
    if t1.left is not None and t2.left is not None:
        newNode = TreeNode(t1.left.val + t2.left.val)
        print(newNode.val)
        newTree.left = newNode
        overlapTraverse(t1.left, t2.left, newTree.left)
    elif t1.right is not None and t2.right is not None:
        newNode = TreeNode(t1.right.val + t2.right.val)
        print(newNode.val)
        newTree.right = newNode
        overlapTraverse(t1.right, t2.right, newTree)
    elif t1.left is None and t2.left is not None:
        newTree.left = TreeNode(t2.left.val)
        print(newTree.left.val)
    elif t1.left is not None and t2.left is None:
        newTree.left = TreeNode(t1.left.val)
        print(newTree.left.val)
    elif t1.right is None and t2.right is not None:
        newTree.right = TreeNode(t2.right.val)
        print(newTree.right.val)
    elif t1.right is not None and t2.right is None:
        newTree.right = TreeNode(t1.right.val)
        print(newTree.left.val)
    return newTree


def traverseTreePreOrder(root):
    if root is not None:
        print(root.val)
        traverseTreePreOrder(root.left)
        traverseTreePreOrder(root.right)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)

n1.left = n2
n1.right = n3
n2.left = n4

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)

t1.left = t2
t1.right = t3

arr = []
# traverseTreePreOrder(n1)
obj = Solution()
obj.mergeTrees(n1, t1)
