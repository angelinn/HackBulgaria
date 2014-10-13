def count_vowels(string):
    vowels = ['a', 'e', 'o', 'u', 'i', 'y', 'A', 'E', 'O', 'U', 'I', 'Y']
    vowels_count = 0

    for each in vowels:
        for char in string:
            if each == char:
                vowels_count += 1

    return vowels_count
