class Node():
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

def is_symmetric(root):

    isSymmetric = True

    currentLeftNode = root
    currentRightNode = root

    while currentLeftNode.children and currentRightNode.children:

        # check if both children match

        # set current left and right to the next node

tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print is_symmetric(tree)
# True

        4
     /     \
    3        3
  / | \    / | \
9   4  1  1  4  9