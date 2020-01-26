from random import randint
from sys import sys

def get_string_length():
    '''gets the length of string to output from console'''
    string_length = sys.argv[1:]
    return string_length


def read_file():
    '''reads the words file into memory'''
    filename = "my_massive_list.txt"

    my_massive_list = open("url/share/dict/words", 'r')
    my_words = my_massive_list.readlines()
    my_massive_list.close()
    return my_words


def select_word(my_words):
    '''select a random set of words and store in a data type'''
    rand_index = randint(0, len(my_words) - 1)

    random_word = my_words[rand_index]
    return random_word


def append_string(string_length):
    '''compile string helper function'''
    random_string = ""
    while string_length < 0:
        random_string = select_word()

    pass


def output_string():
    '''output the string'''
    print(select_word())

# hint: look at rearrange() and random_python_quote()


read_file()
# select_word()
output_string()
