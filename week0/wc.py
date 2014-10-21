import sys


def wc(file_to_count, filter_word):
    total = 0

    content = file_to_count.read()

    if filter_word == 'chars':
        total = len(content)

    elif filter_word == 'words':
        content = (content.replace('\n', ' ')).split(' ')

        for each in content:
            if each != '':
                total += 1

    elif filter_word == 'lines':
        total = 1
        for each in content:
            if each == '\n':
                total += 1

    return total


def main():
    file_to_filter = open(sys.argv[1], 'r')
    print(wc(file_to_filter, sys.argv[2]))
    file_to_filter.close()

if __name__ == '__main__':
    main()
