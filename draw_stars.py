# x = [4, 6, 1, 3, 5, 7, 25]

# for i in x:
# 	print "*" * i


y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

for i in y:
	if type(i) == int:
		print "*" * i
	if type(i) == str:
		leng = len(i)
		for letter in i:
			print letter * leng
			break