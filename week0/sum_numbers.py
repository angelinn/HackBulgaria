import sys


def sum_numbers(file_name):
    numbers_file = open(file_name, 'r')
    content = numbers_file.read()
    total = 0

    numbers = content.split(' ')
    for each in numbers:
        if each != '':
            total += int(each)

    numbers_file.close()
    return total


def main():
    print(sum_numbers(sys.argv[1]))

if __name__ == '__main__':
    main()
