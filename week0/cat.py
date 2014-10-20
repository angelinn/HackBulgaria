# cat.py
import sys


def read_single_content(filename):
    return filename.read()


def cat(filename):
    print(read_single_content(filename))


def main():
    path = sys.argv[1]
    text_file = open(path, 'r')
    cat(text_file)
    text_file.close()

if __name__ == '__main__':
    main()
