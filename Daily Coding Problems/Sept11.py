class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def traverse(root, currentLevel):
    if root.value == 

def valuesAtHeight(root, height):
    # Fill this in.
    print([4, 5, 7])

    print(Node(4).value)
    traverse(root, 0)

    #     1
    #    / \
    #   2   3
    #  / \   \
    # 4   5   7


a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeight(a, 3))
# [4, 5, 7]
