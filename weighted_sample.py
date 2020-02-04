from random import randint

text = 'one fish two fish red fish blue fish'
word_counts = {'one': 1, 'fish': 4, 'two': 1,
               'red': 1, 'blue': 1}


def sample_by_frequency(histogram):

    # TODO: select a word based on frequency
    # how can we sample words using observed frequencies?
    # randint() for index
    loop_count = 0

    while loop_count < len(word_counts):
        new_list = []
        for word, word_count in histogram.items():
            count = 0
            while word_count > count:
                new_list.append(word)
                count += 1
        loop_count += 1

    print("New List:")
    for word in new_list:
        print(word)

    index = randint(0, len(new_list) - 1)
    print("Random Index is " + str(index))

#     -- in class example --
# random_index = randint(0, sum(histogram.values()))
#  start = 0
#  for k,v in histogram.items():
#    end = start + count
#    if random_index >= start and random_index <= end
#       return word
#     else:
#       start = end ---sorta?---

    return new_list[index]

print('Random Word: ' + sample_by_frequency(word_counts))
