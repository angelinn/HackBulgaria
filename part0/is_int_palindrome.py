def is_int_palindrome(n):
    number_string = str(n)
    return number_string == number_string[::-1]