def product(val, *nums):
	for num in nums:
		val *= num
	return val
print(product(5))  # 5
print(product(5,6,7))  # 210
