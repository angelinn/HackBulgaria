# cat.py
import sys


def cat(filename):
    content = filename.read()
    print(content)

    return content


def main():
    path = sys.argv[1]
    text_file = open(path, 'r')
    cat(text_file)
    text_file.close()

if __name__ == '__main__':
    main()
