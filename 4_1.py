class BST():
	def __init__(self, d, l = None, r = None):
		self.d = d
		self.l = l
		self.r = r

def checkSize(t):
	if t==None:
		return 0
	else:
		return 1 + max(checkSize(t.l), checkSize(t.r))

def checkBalanced(t):
	if t == None:
		return True
	else:
		curDiff = abs(checkSize(t.l) - checkSize(t.r))
		if curDiff > 1:
			return False
		else:
			return checkBalanced(t.l) and checkBalanced(t.r)


#### Test Data

good = BST(0, BST(1, BST(2, BST(3)), BST(4)), BST(5, BST(6)))
bad = BST(0, BST(1, BST(2, BST(3, BST(7))), BST(4)), BST(5, BST(6)))

print "should be True: ", checkBalanced(good)
print "should be False: ", checkBalanced(bad)