# cat2.py
import sys


def main():
    first_path = sys.argv[1]
    second_path = sys.argv[2]

    first_file = open(first_path, 'r')
    second_file = open(second_path, 'r')

    first_content = first_file.read()
    second_content = second_file.read()

    print(first_content + '\n' + second_content)

if __name__ == '__main__':
    main()
