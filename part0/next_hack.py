from is_int_palindrome import is_int_palindrome
from count_substrings import count_substrings


def dec_to_binary(dec):
        return int(bin(dec)[2:])


def next_hack(n):
    i = 0
    while i >= 0:
        if i > n:
            if is_int_palindrome(dec_to_binary(i)) and count_substrings(str(dec_to_binary(i)), '1') % 2 != 0:
                return i

        i += 1

print(next_hack(8031))
