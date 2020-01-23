import sys as sys
from random import shuffle

args_list = sys.argv[1:]
shuffle(args_list)

print("Input: ")
for arg in args_list:
    print(arg)

print(args_list)
