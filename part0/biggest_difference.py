def biggest_difference(arr):
    difference = arr[0] - arr[1]
    length = len(arr)

    for i in range(length):
        for j in range(i + 1, length):
            if abs(arr[i] - arr[j]) > abs(difference):
                difference = arr[i] - arr[j]

            j += 1
        i += 1

    return difference

print(biggest_difference(range(100)))