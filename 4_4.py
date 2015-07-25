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


class LLNode:
	def __init__(self, data = None):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)

class LinkedList:
	def __init__(self, n):
		newNode = LLNode(n)
		self.curNode = newNode
		self.firstNode = newNode
		self.lastNode = newNode
		self.size = 1

	def insert(self, newN):
		if self.lastNode.data == None:
			self.lastNode.data = newN
			return self
		else:
			newNode = LLNode(newN)
			self.lastNode.next = newNode
			self.lastNode = newNode
			self.size += 1
			return self

	def __getitem__(self, i):
		x = 0
		self.curNode = self.firstNode
		while x != i:
			self.curNode = self.curNode.next
			x += 1
		return self.curNode

	def __setitem__(self, i, data):
		x = 0
		self.curNode = self.firstNode
		while x != i:
			self.curNode = self.curNode.next
			x += 1
		self.curNode.data = data
		return self

	def __str__(self):
		tempN = self.firstNode
		result = ""
		while tempN != None:
			if tempN != self.firstNode:
				result += "->"
			result += str(tempN.data)
			tempN = tempN.next
		return result

	def __len__(self):
		return self.size

def getLists(tree):
	ht = len(tree)
	arr = []
	for x in xrange(ht):
		arr.append(LinkedList(None))
	getListsHelper(tree, 0, arr)
	return arr

def getListsHelper(n, i, arr):
	if n == None:
		return 0
	arr[i] = arr[i].insert(n)
	if n.left is not None:
		getListsHelper(n.left, i + 1, arr)
	if n.right is not None:
		getListsHelper(n.right, i + 1, arr)

def printLists(arr):
	result = "["
	for thing in arr:
		result += str(thing) + ", "
	result = result[:-2] + "]"
	print result

### Tests
# testLL = LL(LLNode(1))
# testLL.insert(LLNode(2))
# testLL.insert(LLNode(3))
# print testLL ----- 1->2->3
# print testLL[2] -- 3
# testLL[2] = 4
# print testLL ----- 1->2->4

testNode = Node(1, Node(2, Node(6, Node(7))), Node(3, Node(4), Node(5)))
printLists(getLists(testNode))