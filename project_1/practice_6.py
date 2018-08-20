L = [4, 5, 6, 8, 3, 2, 4, 8]
s = set([])
for num in L:
	if num in s:
		print(num)
	s.add(num)
