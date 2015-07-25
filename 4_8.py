class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def __len__(self):
    if self.data == None:
      return 0
    else:
      ltHt = 0
      rtHt = 0
      if self.left is not None:
        ltHt = len(self.left)
      if self.right is not None:
        rtHt = len(self.right)
      return max(ltHt, rtHt) + 1

  def __str__(self):
    return str(self.data)

def checkSubtree(tree, subtree):
  if subtree == None:
    return True
  else:
    return parseSubtree(tree, subtree)

def parseSubtree(tree1, tree2):
  if tree1 == None:
    return False
  if tree1.data == tree2.data:
    return matchTree(tree1, tree2)
  else:
    return parseSubtree(tree1.left, tree2) or parseSubtree(tree1.right, tree2)

def matchTree(tree1, tree2):
  if tree1 is None and tree2 is None:
    return True
  else:
    if tree1 is None or tree2 is None:
      return False
    else:
      if tree1.data == tree2.data:
        return matchTree(tree1.left, tree2.left) and matchTree(tree1.right, tree2.right)

T1 = Node(4, Node(5, Node(6), Node(7)), Node(8))
T2 = Node(5, Node(6), Node(7))
T3 = Node(8, Node(9))

def tests():
  assert(checkSubtree(T1, T2) == True)
  assert(checkSubtree(T1, T3) == False)
  print "all tests passed"

tests()
