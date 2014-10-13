import sys


def wc(path, filter_word):
    total = 0

    file_to_count = open(path, 'r')
    content = file_to_count.read()
    file_to_count.close()

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
    print(wc(sys.argv[1], sys.argv[2]))

if __name__ == '__main__':
    main()
