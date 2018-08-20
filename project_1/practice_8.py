import math

def quadratic(a, b, c):
	if not all(isinstance(i, (int, float)) for i in [a, b, c]):
		raise TypeError('Input numbers only!')
	answer1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
	answer2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
	return answer1, answer2
print(quadratic(2, 3, '1')) # test if you get (-0.5, -1.0)
