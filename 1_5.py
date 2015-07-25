def compress(x, y = "", l = 0):
	print "x = ", x, " y = ", y, " lx = ", l, " ly = ", len(y)
	if x == "":
		if len(y) > l:
			return decompress(y)
		else:
			return y
	elif len(x) == 1:
		if y == "":
			return x
		elif x == y[-2]:
			y += str(int(y[-1]) + 1)
			y = y[:-2] + y[-1]
			return compress("", y, l + 1)
		else:
			y += x
			y += "1"
			return compress("", y, l + 1)
	else:
		if y == "":
			y += x[0]
			y += "1"
			return compress(x[1:], y, l + 1)
		else:
			nC = x[0]
			if y[-2] == nC:
				y += str(int(y[-1]) + 1)
				y = y[:-2] + y[-1]
			else:
				y += nC
				y += "1"
			return compress(x[1:], y, l + 1)

def decompress(x):
	y = ""
	while x != "":
		y += x[0]*(int(x[1]))
		x = x[2:]
	return y

print compress("aabcccccaaabe")
#print compress("abcc")