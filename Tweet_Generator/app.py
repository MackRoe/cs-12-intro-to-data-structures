from flask import Flask
from word_frequency import histogram
from weighted_sample import sample_by_frequency
from markov import MarkovChain

app = Flask(__name__)


@app.route('/')  # see gallary
def make_the_words():
    # build Histogram
    # my_file = open("./words.txt", "r")
    # # absolute path -> ./file.ext ## more fuctional for live deploy
    # lines = my_file.readlines()
    filename = "transient.txt"
    lines = open(filename, "r").readlines()
    transient_txt_words = []  # word_list

    for line in lines:
        wordslist = line.split(' ')
        for word in wordslist:
            word = word.strip(' . , ;" \n _ ?')

            transient_txt_words.append(word)

    my_histogram = histogram(transient_txt_words)

# put together words into a sentence
    sentence = ''
    num_words = 10
    ''' # comment out to impliment markov
    for i in range(num_words):
        word = sample_by_frequency(my_histogram)
        sentence = sentence + " " + word '''

    # uncomment to impliment markov
    markovchain = MarkovChain(transient_txt_words)
    sentence = markovchain.walk(num_words)
    return sentence

# potential terminal syntax for heroku deployment
# http://clouddatafacts.com/heroku/heroku-flask/heroku_flask_getting_started.html

if __name__ == '__main__':
    app.run(debug=True)
