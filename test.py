from random import randint

filename = "words.txt"

my_file = open(filename, "r")

lines = my_file.readlines()


my_file.close

random_index = randint(0, len(lines)-1)
print(lines[random_index])
