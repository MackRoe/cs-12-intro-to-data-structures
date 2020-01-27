from random import randint
import sys as sys
import random

arguments = int(sys.argv[1])
print(arguments)

filename = "/usr/share/dict/words"

my_file = open(filename, "r")

lines = my_file.readlines()


def rearrange_words():
    for rand_arg in range(arguments):
        rand_words = random.randint(1, len(lines) - 1)
        print(lines[rand_words])


rearrange_words()
