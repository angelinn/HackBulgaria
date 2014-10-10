from is_prime import is_prime

def number_of_divisors(n):
	divisors = 0
	i = 1

	while i <= n:
		if n % i == 0:
			divisors += 1

		i += 1

	return divisors

def prime_number_of_divisors(n):
	return is_prime(number_of_divisors(n))

print(prime_number_of_divisors(9))