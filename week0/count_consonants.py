from count_vowels import count_vowels


def count_consonants(string):
    letters = 0
    for char in string:
        if char.isalpha():
            letters += 1

    return letters - count_vowels(string)
