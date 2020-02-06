from flask import Flask
from word_frequency import histogram
from weighted_sample import sample_by_frequency

app = Flask(__name__)


@app.route('/')
def make_the_words():
    # build Histogram
    # my_file = open("./words.txt", "r")
    # # absolute path -> ./file.ext ## more fuctional for live deploy
    # lines = my_file.readlines()
    filename = "transient.txt"
    lines = open(filename, "r").readlines()
    transient_txt_words = []

    for line in lines:
        wordslist = line.split(' ')
        for word in wordslist:
            word = word.strip(' . , ;" \n _')
            transient_txt_words.append(word)

    my_histogram = histogram(transient_txt_words)

    word = sample_by_frequency(my_histogram)
    return word


if __name__ == '__main__':
    app.run(debug=True)
