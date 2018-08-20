def fib(n):
	if n <= 0:
		raise ValueError('invalid input')
	if n <= 2:
		return 1
	return fib(n - 1) + fib(n - 2)
print(fib(8))  # 21