# generate_numbers.py
import sys
from random import randint


def generate_numbers(n, wfile):
    content = ""

    for i in range(n):
        content += str(randint(1, 1000)) + ' '

    wfile.write(content)


def main():
    path = sys.argv[1]
    wfile = open(path, 'w')

    count = int(sys.argv[2])

    generate_numbers(count, wfile)
    wfile.close()

if __name__ == '__main__':
    main()
