import string
from statistics.popularity import score_all
import util
from word.rules import Rule, matches

def scoring_mode():
    """
    Runs the application in scoring mode to generate lexicon.txt
    """
    words = util.read_words()
    scores = score_all(words)
    util.write_lexicon(scores)
    words = util.read_lexicon()
    util.print_lexicon(words)


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

    rules = []

    lexicon = util.read_lexicon()
    lexicon = util.sort_lexicon(lexicon)
    guesses = []
    for key in lexicon.keys():
        if matches(rules, key):
            guesses.append(key[::-1])

    fixed = []
    guesses.sort()
    for i in guesses:
        fixed.append(i[::-1])

    util.print_list(fixed)
