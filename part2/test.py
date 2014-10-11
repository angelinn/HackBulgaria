import sys
from random import randint


def writing(str):
    filee = open("test.txt", 'w')
    filee.write(str(randint(1, 20)))

writing(sys.argv[1])
