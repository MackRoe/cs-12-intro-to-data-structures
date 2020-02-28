from dictogram import Dictogram

class MarkovChain:

    def __init__(self, word_list):


        #The Markov chain will be a dictionary of dictionaries
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
        self.word_list = word_list
        self.markov_chain = self.build_markov(word_list)
        self.first_word = list(self.markov_chain.keys())[0]

    def build_markov(self, word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1):
            #get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            if current_word in markov_chain.keys():  # already there
                # get the histogram for that word in the chain
                histogram = markov_chain[current_word]
                # add to count
                histogram.dictionary_histogram[next_word] = histogram.dictionary_histogram.get(next_word, 0) + 1
            else:  # first entry
                markov_chain[current_word] = Dictogram([next_word])
                # look at how Dictogram class is implimented

        return markov_chain

    def walk(self, num_words):
        '''generates a string of words num_words long using the markov chain'''
        # loop number of times indicated by num_words variable
        # first add first_word to string
        walked_string = self.first_word
        chain = self.build_markov(self.word_list)

        word = self.first_word
        for i in range(num_words):
            dictogram = chain[word]
            # select a random word from weighted sample of potential next words
            word = self.dictionary_histogram.sample()
            #   get random word from weighted sample generated from Dictogram
            #       associated with the indicated key
            walked_string += word
            # append selected word to string
        return walked_string

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.dictionary_histogram)



markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
markov_chain.print_chain()
print(markov_chain.walk(10))
