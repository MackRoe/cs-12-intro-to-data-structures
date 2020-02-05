# from dictogram import histogram <== check import

# we are building a histogram that looks like this
# [["one", 1], ["fish", 4], ["red", 1]]
# it is a list of lists, or an outer list that contain
# multiple smaller inner lists each with a word as the first item
# and the word's count as the second item

# This helper function searches for a given word in a given listogram
# it returns the index of the inner list if the word is found, and some
# non valid index value like -1 or "nope" if not

def get_index(word, listogram):
    # TODO: loop through each item in the input listogram

    # TODO: create a variable that keeps track of the index of the
    # current item we are checking

    # TODO: each item is a list where the first element is
    # the word and the second element is the count

    # TODO: check if the word in the listogram is equal to the
    # word parameter (the word we are searching for)
    # if it is, we have found it and can return the index
    # otherwise we add one to the current index and keep searching
    # if we never find the word then we can return our non valid index value
    pass


def listogram(lines):
    listogram = []

    # TODO: loop through each word in lines

    # TODO: call get_index() and save the result to a variable

    # TODO: if the result is the non valid index value then
    # we know the word was not found and this is the first time we have seen
    # the word in this case we will append a new inner list with the word and a
    # count of 1, otherwise we have seen the word before and we need to use the
    # result which will be the index of the inner list to update the count
    # by 1 in that inner list

    # TODO: return the listogram


lines = open("words.txt", "r").readlines()
print(listogram(lines))
