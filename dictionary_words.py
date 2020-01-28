from random import randint
import sys as sys


'''gets the length of string to output from console'''
string_length = int(sys.argv[1])


'''reads the words file into memory'''
filename = "/usr/share/dict/words"

my_massive_list = open(filename, 'r')
my_words = my_massive_list.readlines()
# my_massive_list.close()


def select_word(my_words):
    '''select a random set of words and store in a data type'''
    rand_index = randint(1, len(my_words) - 1)

    random_word = my_words[rand_index]
    return random_word


def append_string(string_length):
    '''compile string helper function'''
    random_string = ""
    while string_length > 0:
        random_string = random_string + select_word(my_words)
        string_length -= 1
    print(random_string)


def output_string():
    '''output the string'''
    print(select_word(my_words))

# hint: look at rearrange() and random_python_quote()

# select_word()
# output_string()

append_string(string_length)
