from random import randint


class Listogram:

    def __init__(self, word_list):
        '''Initializes the listogram properties'''

        self.word_list = word_list

        self.list_histogram = self.build_listogram()

        self.tokens = self.get_num_tokens()
        self.types = self.unique_words()

    def get_index(self, word, list_histogram):
        '''searches in the list histogram parameter and returns the index of
        the inner list that contains the word if present'''
        # TODO: use your get_index function as a starting point to complete
        # this method
        current_index = 0
        for item in list_histogram:
            # print(item)
            # TODO: check if the word in the listogram is equal to the
            # word parameter (the word we are searching for)
            if item[0] == word:
                # if it is, we have found it and can return the index
                return current_index
            else:
                # otherwise we add one to the current index and keep searching
                current_index += 1
        # if word not found, return non valid index value
        return -1

    def build_listogram(self):
        '''Creates a histogram list of lists using the word_list property and
        returns it'''
        lines = self.word_list
        # TODO: use your listogram function as a starting point to complete
        # this method
        listogram = []
        # loop through each word in lines
        print('')
        print('>> build_listogram method called <<')
        print(lines)
        for word in lines:

            index = self.get_index(word, listogram)
            # print("listogram in build_listogram() = " + word[index])
            word = word.strip()
            if index == -1:
                listogram.append([word, 1])
            else:
                listogram[index][1] += 1
        print("build_listogram method returns: ")
        print(listogram)
        print(">> end build_listogram <<")
        return listogram

    def get_num_tokens(self):
        '''gets the number of tokens in the listogram'''

        tokens = 0
        for item in self.list_histogram:
            tokens += item[1]
        return tokens

    def frequency(self, word):
        '''returns the frequency or count of the given word in the list of
        lists histogram'''
        # TODO: use your frequency and get_index function as a starting point
        # to complete this method
        # You will need to adapt it a little bit to work with listogram
        #count = 0
        #main_list_index = 0
        # find match for word in list.sublist[sublist_key_index]
        '''while count < len(self.list_histogram) - 1:
            print("Frequency function activated.")
            for inner_list in self.list_histogram[main_list_index]:
                print("inner list loop " + str(count))
                for item in inner_list:
                    print("Item in inner list: ")
                if inner_list[0] == word.lower():
                    frequency_of_word = inner_list[1]
                count += 1'''
        index_of_inner_list = self.get_index(word, self.list_histogram)
        inner_list = self.list_histogram[index_of_inner_list]
        return inner_list[1]

    def unique_words(self):
        '''returns the number of unique words in the list of lists histogram'''
        # TODO: use your unique words function as a starting point to complete
        # this method
        # You will need to adapt it a little bit to work with listogram
        number_of_unique_words = len(self.list_histogram)
        return number_of_unique_words

    def sample(self):
        '''Randomly samples from the list of list histogram based on the
        frequency, returns a word'''

        # TODO: use your sample function as a starting point to complete this
        # method
        # You will need to adapt it a little bit to work with listogram

        new_list = []
        for sublist in self.list_histogram:
            word = sublist[0]
            word_count = sublist[1]
            count = 0
            while word_count > count:
                new_list.append(word)
                count += 1

        # print("New List:")
        # for word in new_list:
        #     print(word)

        index = randint(0, len(new_list) - 1)
        # print("Random Index is " + str(index))

        return new_list[index]


# following functions are outside of class
def print_listogram(word_list):
    '''Creates a list based histogram (listogram) and then prints out its
    properties and samples from it'''

    print()
    print(">>> print_listogram method called <<<")
    print('List of Lists Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    listogram = Listogram(word_list)
    print('listogram: {}'.format(listogram.list_histogram))
    print('{} tokens, {} types'.format(listogram.tokens, listogram.types))
    for word in word_list[-2:]:
        freq = listogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print(">> end print_listogram method <<")
    print()
    print_dictogram_samples(listogram)


def print_dictogram_samples(listogram):
    '''Compares sampled frequency to observed frequency'''

    print('')
    print('>>> print_dictogram_samples method called <<<')
    print('List of Lists Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [listogram.sample() for _ in range(10000)]
    samples_hist = Listogram(samples_list)
    print('samples: {}'.format(samples_hist.list_histogram))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for item in listogram.list_histogram:
        word = item[0]
        count = item[1]
        # Calculate word's observed frequency
        observed_freq = count / listogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
              + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
              + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
              + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()

print_listogram(['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'])
