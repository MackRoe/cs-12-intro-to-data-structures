from random import randint

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!",
          "This isn't my nose. It's a false nose.")


def random_python_quote():
    rand_index = randint(0, len(quotes) - 1)
    return quotes[rand_index]


if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)
