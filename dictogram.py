# this is the dictionary way of building a histogram for reference
def histogram(lines):
    histogram = {}
    for word in lines:
        word = word.rstrip()
        if word in histogram.keys():
            histogram[word] = histogram[word] + 1
        else:
            histogram[word] = 1
    return histogram
