from fibonacci_lists import fibonacci_lists


def member_of_nth_fibonacci_lists(listA, listB, needle):
    i = 1

    while True:
        if needle == fibonacci_lists(listA, listB, i):
            return True

        if len(needle) <= len(fibonacci_lists(listA, listB, i)):
            return False

        i += 1
