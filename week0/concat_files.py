import sys


def concat_files(path_one, path_two):
    destination = "MEGATRON"

    file_one = open(path_one, 'r')
    file_two = open(path_two, 'r')

    content_one = file_one.read()
    content_two = file_two.read()

    file_one.close()
    file_two.close()

    megatron = open(destination, 'w')
    megatron.write(content_one + '\n' + content_two)

    megatron.close()


def main():
    concat_files(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
