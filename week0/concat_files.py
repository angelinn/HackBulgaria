import sys


def concat_files(file_one, file_two):
    destination = "MEGATRON"

    megatron = open(destination, 'w')
    megatron.write(file_one.read() + '\n' + file_two.read())

    megatron.close()


def main():
    file_one = open(sys.argv[1], 'r')
    file_two = open(sys.argv[2], 'r')

    concat_files(file_one, file_two)

    file_one.close()
    file_two.close()

if __name__ == '__main__':
    main()
