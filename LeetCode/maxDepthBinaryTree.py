# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        depthList = []
        stk = [root]
        currDepth = 1

        while stk:
            currNode = stk.pop()
            print("current node: ", currNode.val)
            print("current depth: ", currDepth)
            if currNode.right is None and currNode.left is None:
                depthList.append(currDepth)
                print("depth list: ", depthList)
                # currDepth -= 1
                continue
            currDepth += 1
            if currNode.right:
                stk.append(currNode.right)
            if currNode.left:
                stk.append(currNode.left)
        return max(depthList)

# BLAGH NOT PASSING ALL TEST CASES UGHHHHH


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
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.right = TreeNode(7)
# root.right.left = TreeNode(15)

obj = Solution()
ans = obj.maxDepth(root)
print("ans: ", ans)
