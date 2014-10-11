# generate_numbers.py
import sys
from random import randint


def main():
    path = sys.argv[1]
    count = sys.argv[2]
    print(path)
    print(count)

    generate_numbers(count, path)


def generate_numbers(n, path):
    wfile = open(path, 'w')
    content = ""

    for i in range(n):
        print(i)
        content += str(randint(1, 1000))
        content += ' '

    wfile.write(content)
    wfile.close()

if __name__ == '__main__':
    main()
