# generate_numbers.py
import sys
from random import randint


def generate_numbers(n, path):
    wfile = open(path, 'w')
    content = ""

    print(n)
    for i in range(n):
        content += str(randint(1, 1000)) + ' '

    wfile.write(content)
    wfile.close()


def main():
    path = sys.argv[1]
    count = int(sys.argv[2])

    generate_numbers(count, path)

if __name__ == '__main__':
    main()
