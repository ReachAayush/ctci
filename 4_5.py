class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def checkBST(tree, min_val, max_val):
  if tree == None:
    return True
  if tree.data <= min_val or tree.data >= max_val:
    return False
  else:
    if not checkBST(tree.left, min_val, tree.data) or not checkBST(tree.right, tree.data, max_val):
      return False
    return True

min_val = -1
max_val = 12

good = Node(6, Node(4, Node(3), Node(5)), Node(8, Node(7), Node(10, Node(9), Node(11))))
print checkBST(good, min_val, max_val) ## True

bad = Node(6, Node(4, Node(3), Node(5)), Node(7, Node(8), Node(10)))
print checkBST(bad, min_val, max_val) ## False
