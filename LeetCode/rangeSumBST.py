# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root, L, R):
        sum = 0
        stack = []
        currentNode = root

        # keep iterating the BST until stack is empty and current is NULL
        # this means we have seen all nodes and emptied the stack
        # This is In Order Traversal (L-N-R)
        while True:

            # keep going left and add to the stack
            if currentNode is not None:
                stack.append(currentNode)
                currentNode = currentNode.left

            # Ive reached the end of the left, so pop and go right
            # if there things on the stack, do this
            elif(stack):
                num = stack.pop()
                # check if within range
                if num.val >= L and num.val <= R:
                    sum += num.val
                    print(sum)
                else:
                    currentNode = num.right

            # Now the node is none and the stack is empty, so we are done
            else:
                break


""" Constructed binary tree is 
            1 
          /   \ 
         2     3 
       /  \ 
      4    5   """

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(10)
root.left.right = TreeNode(5)

obj = Solution()
obj.rangeSumBST(root, 2, 11)
