"""
Calculates stats on how popular words are.
Used for deteremining likelyhood of a word being an answer.
"""
from tokenize import String
from time import sleep
import requests
import math
from word.rules import Rule


def score_all(words):
    """
    Returns a scored list of all words in the input words list. Scored list is of format {'word': string, 'score': int}

    Keyword Arguments:
    words -- a list of words to score
    """
    res = {}
    for word in words:
        res[word] = score(word)
    return res


def score(word: String):
    """
    Returns the score (int) of a single word.

    Keyword Arguments:
    word -- The word to store
    """
    sleep(0.05)  # maybe not necessary, but trying to be polite
    max_res = 50  # number of results max
    request = f"https://api.onelook.com/words?max={max_res}&nonorm=1&k=rz_wke&rel_wke={word}"
    response = requests.get(request)
    score = sum([i['score'] for i in response.json()])
    print(f"{word}|{score}")
    return score


def scale(num_string):
    num = int(num_string)
    return math.log(num) if num != 0 else 0


def letter_popularity(lexicon):
    scores = {}
    for word in lexicon.keys():
        for letter in set(word):
            scores[letter] = scores[letter] + \
                scale(lexicon[word]) if letter in scores else scale(
                    lexicon[word])
    return {k: v for k, v in sorted(scores.items(), key=lambda item: item[1])}


def score_lexicon(lexicon):
    """
    Provides a score for the remaining lexicon.
    """
    s = 0
    for word in lexicon.keys():
        s += score(lexicon[word])
    return s

def top_three(words, lexicon):
    best_one = 'UNKNOWN'
    top_score = 0
    best_two = 'UNKNOWN'
    best_three = 'UNKNOWN'
    for word in words:
        score = int(lexicon[word])
        if score > top_score:
            top_score = score
            best_three = best_two
            best_two = best_one
            best_one = word
    print(f"Best pure guesses: {best_one}, {best_two}, {best_three}")


def score_positionally(words, lexicon):
    best = 'UNKNOWN'
    last = 0
    for word in words:
        total = 0
        for i in range(0, 5):
            letter = word[i]
            rule = Rule.word().has(letter).at(i)
            for key in lexicon.keys():
                if rule.eval(key):
                    total += scale(lexicon[key])

        if total > last:
            last = total
            best = word
            print(f"{word}|{total}")
    print(f"Best Positionally: {best}")


def score_yellow(words, letters):
    best = 'UNKNOWN'
    last = 0
    for word in words:
        total = 0
        for letter in set(word):
            total += int(float(letters[letter]))
        if total > last:
            last = total
            best = word
            print(f"{word}|{total}")
    print(f"Most Yellows: {best}")
