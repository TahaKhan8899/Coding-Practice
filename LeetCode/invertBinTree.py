# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invertTree(root):

    if root:
        print(root.val)

        swapChildren(root)

        # stk = []
        que = []
        if root.left:
            # stk.append(root.left)
            que.append(root.left)
        if root.right:
            # stk.append(root.right)
            que.append(root.right)

        while que:
            # node = stk.pop()
            node = que.pop(0)
            print(node.val)
            swapChildren(node)

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

    print("===================")
    printTree(root)
    return root


def swapChildren(node):
    if node.right and node.left:
        print(node.left.val, "<--- ", node.val, " --->", node.right.val)
        tmp = node.right
        node.right = node.left
        node.left = tmp
        print(node.left.val, "<--- ", node.val, " --->", node.right.val)

    if node.right and not node.left:
        print(node.left, "<--- ", node.val, " --->", node.right.val)
        tmp = node.right
        node.right = None
        node.left = tmp
        print(node.left.val, "<--- ", node.val, " --->", node.right)
    if node.left and not node.right:
        tmp = node.left
        node.left = None
        node.right = tmp

    # return node


def printTree(root):

    if root:
        print(root.val)

        que = []
        if root.left:
            que.append(root.left)
        if root.right:
            que.append(root.right)

        while que:
            node = que.pop(0)
            print(node.val)

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)


def test1():

        #         4
        #       /   \
        #      2     7
        #     / \   / \
        #    1   3 6   9

    n1 = TreeNode(4)

    n2 = TreeNode(2)

    n3 = TreeNode(7)

    n4 = TreeNode(1)
    n4.right = None
    n4.left = None

    n5 = TreeNode(3)
    n5.right = None
    n5.left = None

    n6 = TreeNode(6)
    n6.right = None
    n6.left = None

    n7 = TreeNode(9)
    n7.right = TreeNode(10)
    n7.left = None

    n1.right = n3
    n1.left = n2
    n2.right = n5
    n2.left = n4
    # n3.right = n7
    n3.left = n6

    invertTree(n1)


def test2():

    n1 = TreeNode(1)
    n2 = TreeNode(2)

    n1.right = n2

    invertTree(n1)


# print("test1: ")
# test1()
print("test2: ")
test2()
