def sum_of_digits(n):
	if n == 0:
		return 0
	if(n < 0):
		n *= (-1)

	return sum_of_digits(n // 10) + n % 10
