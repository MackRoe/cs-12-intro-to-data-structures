from random import randint


def read_file():
    '''reads the words file into memory'''
    filename = "my_massive_list.txt"

    my_massive_list = open("url/share/dict/words", 'r')
    my_words = my_massive_list.readlines()
    my_massive_list.close()


def select_words():
    '''select a random set of words and store in a data type'''
    rand_index = randint(0, len(my_words) - 1)

    random_word_string = my_words[rand_index]
    return random_word_string


def output_string():
    '''output the string'''
    print(select_words())

# hint: look at rearrange() and random_python_quote()


read_file()
select_words()
output_string()
