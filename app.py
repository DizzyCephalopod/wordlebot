import string
from statistics.popularity import score_all
from util import read_words, read_lexicon, print_lexicon


def scoring_mode():
    """
    Runs the application in scoring mode to generate lexicon.txt
    """
    words = read_words()
    scores = score_all(words)
    print_lexicon(scores)  # todo, dump these in lexicon.txt


def interactive_mode():
    """
    Runs the game in interactive mode.
    In this mode, the user will manually enter the results given by the game.
    The bot will then recommend a move. Repeat.
    """
    pass


def backtest_mode(answer: string):
    """
    Runs the appliation in backtest mode.
    In this mode, you pass in an answer, and the game will play itself and print out the result.
    """
    pass


if __name__ == '__main__':
    # scoring_mode()
    lexi = read_lexicon()
    print_lexicon(lexi)
