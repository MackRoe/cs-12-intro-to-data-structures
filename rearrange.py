import sys as sys
from random import randint

list = sys.argv[1:]

for i in range(len(list)):
    rand_index = randint(0, len(list)-1)
    print(list[rand_index])
