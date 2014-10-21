import sys


def sum_numbers(numbers_file):
    content = numbers_file.read()
    total = 0

    numbers = content.split(' ')
    for each in numbers:
        if each != '':
            total += int(each)

    return total


def main():
    numbers_file = open(sys.argv[1], 'r')
    print(sum_numbers(numbers_file))
    numbers_file.close()

if __name__ == '__main__':
    main()
