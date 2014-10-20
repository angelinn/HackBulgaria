# cat2.py
import sys


def read_multiple_content(*filenames):
    content = ''

    for i in range(len(filenames)):
        content += filenames[i].read()

        if i != len(filenames) - 1:
            content += '\n'

    return content


def cat2(*filenames):
    print(read_multiple_content(*filenames))


def main():
    first_path = sys.argv[1]
    second_path = sys.argv[2]

    first_file = open(first_path, 'r')
    second_file = open(second_path, 'r')

    cat2(first_file, second_file)

    first_file.close()
    second_file.close()

if __name__ == '__main__':
    main()
