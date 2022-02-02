import string
import statistics.popularity as stats
import util
from word.rules import Rule, matches


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
    pass


def backtest_mode(answer: string):
    """
    Runs the appliation in backtest mode.
    In this mode, you pass in an answer, and the game will play itself and print out the result.
    """
    pass


def eval_all(lexicon, rules):
    filtered = {}
    for word in lexicon.keys():
        if matches(rules, word):
            filtered[word] = lexicon[word]
    return filtered


if __name__ == '__main__':
    lexicon = util.read_lexicon()
    words = util.read_words()
    letters = util.read_letters()

    rules = []
    rules.append(Rule.word().has('E').anywhere())
    rules.append(Rule.word().has('O').anywhere())
    rules.append(Rule.word().has('S').anywhere())
    rules.append(Rule.word().has('T').anywhere())
    rules.append(Rule.word().has('H').anywhere())

    # an elimination guess is one where 

    lexicon = eval_all(lexicon, rules)
    print("--------")
    util.print_dict(lexicon)
    print("--------")
    words = [w for w in lexicon.keys()]

    stats.score_yellow(words, stats.letter_popularity(lexicon))
    stats.score_positionally(words, lexicon)
