def sevens_in_a_row(arr, n):
	target = 7

	for i in range(len(arr) - 1):
		if arr[i] == target:
			times_met = 0

			for j in range(n):
				if i == len(arr):
					break

				if arr[i] == target:
					times_met += 1
					if times_met == n:
						return True
				else:
					break

				j += 1
				i += 1

	return False

print(sevens_in_a_row([7,2,1,6,2], 1))