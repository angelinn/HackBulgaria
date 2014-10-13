# cat.py
import sys


def main():
    path = sys.argv[1]
    text_file = open(path, 'r')

    content = text_file.read()
    text_file.close()
    print(content)

if __name__ == '__main__':
    main()
