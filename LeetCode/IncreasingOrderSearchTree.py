class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root):

        current = root
        stack = []

        newRoot = TreeNode(None)
        newCurrent = newRoot

        while True:

            if current is not None:
                stack.append(current)
                current = current.left

            elif(stack):
                current = stack.pop()
                newCurrent.right = current
                newCurrent = newCurrent.right
                print("NewTree: ", newCurrent.val)
                # print(current.val, end=" ")  # Python 3 printing

                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                current = current.right

            else:
                break

        return newRoot.right

        # left
        # node
        # right


#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(8)

obj = Solution()
ans = obj.increasingBST(root)

while(ans is not None):
    print(ans.right.val)
    ans = ans.right
