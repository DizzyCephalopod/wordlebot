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


def filter(lexicon, rules):
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
    rules.append(Rule.word().does_not_have('A'))
    rules.append(Rule.word().has('E').at(1))
    rules.append(Rule.word().has('R').anywhere())
    rules.append(Rule.word().does_not_have('O'))
    rules.append(Rule.word().does_not_have('S'))
    rules.append(Rule.word().has('U').anywhere())
    rules.append(Rule.word().does_not_have('N'))
    rules.append(Rule.word().does_not_have('L'))
    rules.append(Rule.word().does_not_have('I'))
    rules.append(Rule.word().has('T').at(4))

    lexicon = filter(lexicon, rules)
    print("--------")
    util.print_dict(lexicon)
    print("--------")
    words = [w for w in lexicon.keys()]

    stats.score_yellow(words, letters)
    stats.score_positionally(words, lexicon)
