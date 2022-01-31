"""
#Common Utilities
Utilities used throughout the rest of the app.
"""

def print_list(arr):
    """ Prints a list one item per line
    """
    for i in arr:
        print(i)

def print_lexicon(lexicon):
    """ Prints a list of scores.
    A score is in the format {'word': string, 'score': int}
    """
    for word in lexicon.keys():
        print(f"{word}|{lexicon[word]}")

def read_file(filename):
    """ Reads all the lines in a file.
    """
    with open(filename, encoding='utf-8') as f:
        lines = []
        for line in f:
            lines.append(line.strip())
        return lines

def read_words():
    """
    Returns an array of all words in words.txt
    """
    lines = read_file('resources/words.txt')
    words = []
    for line in lines:
        words.extend(line.split(' '))
    return words

def read_lexicon():
    """
    Returns the dict of {'word': string, 'score': int} represented by lexicon.txt
    """
    lines = read_file('resources/lexicon.txt')
    lexicon = {}
    for line in lines:
        parts = line.strip().split('|')
        word = parts[0]
        score = parts[1]
        lexicon[word] = score
    return lexicon

def write_lexicon(lexicon):
    """
    Writes the scored words down as a lexicon.
    """
    with open('resources/lexicon.txt', 'w', encoding="utf-8") as _file:
        for word in lexicon.keys():
            _file.write(f"{word}|{lexicon[word]}")
            _file.write('\n')

def sort_lexicon(lexicon):
    d = {}
    for i in sorted(lexicon.items(), key = lambda i:(i[0], i[1])):
        d[i[0]] = i[1]
    return d
