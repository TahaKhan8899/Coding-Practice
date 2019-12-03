# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):

        stack = [root]
        levelArray = [[root.val]]

        while(len(stack) > 0):
            curNode = stack.pop()
            print(curNode.val)
            if curNode.left or curNode.right:
                stack.append(curNode.left)
                stack.append(curNode.right)
                children = [curNode.left.val, curNode.right.val]
                print(children[0], children[1])
                levelArray.append(children)

        print("levelArray: ", levelArray)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
obj = Solution()
obj.levelOrder(root)
