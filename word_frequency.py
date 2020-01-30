import sys as sys

'''gets the word for which frequency of occurance value is sought'''
search_word = str(sys.argv[1])

filename = "transient.txt"
lines = open(filename, "r").readlines()
transient_txt_words = []


for line in lines:
    wordslist = line.split(' ')
    for word in wordslist:
        word = word.strip(' . , ;" \n _')
        transient_txt_words.append(word)
# print(transient_txt_words)
# input()

# print('transient_txt_words contains: ')
# for word in transient_txt_words:
#     print(word)

my_histogram = {}


def histogram():
    '''function which takes a source_text argument (can be either a filename or
    the contents of the file as a string, your choice) and return a histogram
    data structure that stores each unique word along with the number of times
    the word appears in the source text'''
    for word in transient_txt_words:
        word = word.strip(' . , ; " \n _')
        # print(word)

        my_histogram[word] = my_histogram.get(word, 0)+1
    # print(my_histogram)  # print to test
    return my_histogram


def unique_words(any_histogram):
    '''function that takes a histogram argument and returns the total count of
    unique words'''
    number_of_unique_words = len(any_histogram)
    return number_of_unique_words


def frequency(word, any_histogram):
    '''function that takes a word and histogram argument and returns the number
    of times that word appears in a text.'''
    frequency_of_word = any_histogram[word]
    return frequency_of_word


histogram()

print('Histogram contains ' + str(unique_words(my_histogram)) + ' unique words')
print(search_word + ' appears ' + str(frequency(search_word, my_histogram)) + ' times.')
