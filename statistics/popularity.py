"""
Calculates stats on how popular words are.
Used for deteremining likelyhood of a word being an answer.
"""
from tokenize import String
import requests

def score_all(words):
    """
    Returns a scored list of all words in the input words list. Scored list is of format {'word': string, 'score': int}

    Keyword Arguments:
    words -- a list of words to score
    """
    res = []
    for word in words:
        res.append({word, score(word)})
    return res

def score(word: String):
    """
    Returns the score (int) of a single word.\

    Keyword Arguments:
    word -- The word to store
    """
    max_res = 50 # number of results max
    request = f"https://api.onelook.com/words?max={max_res}&nonorm=1&k=rz_wke&rel_wke={word}"
    response = requests.get(request)
    return sum([i['score'] for i in response.json()])
