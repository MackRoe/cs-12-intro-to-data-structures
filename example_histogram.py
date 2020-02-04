# FOR REFERENCE ONLY
# TA plz do not evaluate

filename = "words.txt"
lines = open(filename, "r")

word_histogram = {}

for word in lines:
    word = word.rstrip()
    # TODO: add code to increase the count in the histogram
    # for the given word
    # -- long way ---
    # if word not in word_histogram:
    #     word_histogram[word] = 1
    # else:
    #     word_count_value = word_histogram.get(word)
    #     word_count_value += 1
    #     word_histogram[word] = word_count_value

    # one-liner:
    word_histogram[word] = word_histogram.get(word, 0)+1

print(word_histogram)
