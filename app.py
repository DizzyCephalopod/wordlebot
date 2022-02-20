"""
The main application.
"""
import string
import statistics.popularity as stats
import re
import util
from word.rules import RuleBuilder, matches


def scoring_mode():
    """
    Runs the application in scoring mode to generate lexicon.txt
    """
    words = util.read_words()
    scores = stats.score_all(words)
    util.write_lexicon(scores)
    words = util.read_lexicon()
    util.print_dict(words)


def interactive_mode():
    """
    Runs the game in interactive mode.
    In this mode, the user will manually enter the results given by the game.
    The bot will then recommend a move. Repeat.
    """
    lexicon = util.read_lexicon()
    words = util.read_words()
    letters = util.read_letters()

    builder = RuleBuilder()

    result_expression = re.compile('')
    while True:
        raw = input("Enter result: ").upper()
        if raw == 'QUIT' or raw == 'Q':
            break
        if result_expression.match(raw):
            parsed = raw.split('/')
            word = parsed[0]
            colors = parsed[1]

            builder.append(word, colors)

            rules = builder.build()
            for rule in rules:
                print(rule)

            # an elimination guess is one where

            lexicon = eval_all(lexicon, rules)
            print("--------")
            # util.print_dict(lexicon)
            print("--------")
            words = [w for w in lexicon.keys()]

            stats.score_yellow(words, stats.letter_popularity(lexicon))
            stats.score_positionally(words, lexicon)
            stats.top_three(words, lexicon)
        else:
            print("Enter 'Q' or 'QUIT' to quit.")
            print("Game results are entered in the form of WWWWW/CCCCC")
            print("   W -> a letter in the word")
            print("   / -> delimeter")
            print("   C -> the color of the result")
            print("      B -> Black")
            print("      Y -> Yellow")
            print("      G -> Green")


def backtest_mode(answer: string):
    """
    Runs the appliation in backtest mode.
    In this mode, you pass in an answer, and the game will play itself and print out the result.
    """
    pass


def eval_all(lexicon, rules):
    """
    Eval all the rules
    """
    filtered = {}
    for word in lexicon.keys():
        if matches(rules, word):
            filtered[word] = lexicon[word]
    return filtered


if __name__ == '__main__':
    interactive_mode()
