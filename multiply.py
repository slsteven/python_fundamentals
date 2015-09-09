def multiply(list, num):
	newlist = []
	for i in list:
		newlist.append(i * num)
	return newlist

a = [1, 2, 3, 4]
b = multiply(a, 2)
print b
