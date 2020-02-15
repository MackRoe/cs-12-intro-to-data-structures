from random import randint

word_list = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']


class Dictogram:

    def __init__(self, word_list):
        '''Initializes the dictogram properties'''

        self.word_list = word_list

        self.dictionary_histogram = self.build_dictogram()

        self.tokens = sum(self.dictionary_histogram.values())
        self.types = self.unique_words()

    def build_dictogram(self, word_list):
        '''Creates a histogram dictionary using the word_list property and
        returns it'''
        dictogram = {}
        for word in word_list:
            word = word.strip(' . , ; " \n _ ? !')

        dictogram[word] = dictogram.get(word, 0)+1

        return dictogram

    def frequency(self, word):
        '''returns the frequency or count of the given word in the dictionary
        histogram'''
        frequency_of_word = self.dictionary_histogram[word]
        return frequency_of_word

    def unique_words(self, dictogram):
        '''returns the number of unique words in the dictionary histogram'''
        number_of_unique_words = len(dictogram)
        return number_of_unique_words

    def sample(self, dictogram):
        '''Randomly samples from the dictionary histogram based on the
        frequency, returns a word'''
        loop_count = 0

        while loop_count < len(dictogram):
            new_list = []
            for word, word_count in dictogram.items():
                count = 0
                while word_count > count:
                    new_list.append(word)
                    count += 1
            loop_count += 1

        index = randint(0, len(new_list) - 1)
        word = new_list[index]
        return word


def print_dictogram(word_list):
    '''Creates a dictionary based histogram (dictogram) and then prints out its
    properties and samples from it'''

    print()
    print('Dictionary Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    dictogram = Dictogram(word_list)
    print('dictogram: {}'.format(dictogram.dictionary_histogram))
    print('{} tokens, {} types'.format(dictogram.tokens, dictogram.types))
    for word in word_list[-2:]:
        freq = dictogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_dictogram_samples(dictogram)


def print_dictogram_samples(dictogram):
    '''Compares sampled frequency to observed frequency'''

    print('Dictionary Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [dictogram.sample() for _ in range(10000)]
    samples_hist = Dictogram(samples_list)
    print('samples: {}'.format(samples_hist.dictionary_histogram))
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
    for word, count in dictogram.dictionary_histogram.items():
        # Calculate word's observed frequency
        observed_freq = count / dictogram.tokens
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


print_dictogram(word_list)
