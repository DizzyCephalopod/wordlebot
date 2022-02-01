"""
#Common Utilities
Utilities used throughout the rest of the app.
"""

def print_list(arr):
    """ Prints a list one item per line
    """
    for i in arr:
        print(i)

def print_dict(data):
    """ Prints key value pairs in a dict
    """
    for key in data.keys():
        print(f"{key}|{data[key]}")

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

def read_dict(filename):    
    """
    Returns the dict of {'key': string, 'value': string} in a file
    """
    lines = read_file(filename)
    data = {}
    for line in lines:
        parts = line.strip().split('|')
        word = parts[0]
        score = parts[1]
        data[word] = score
    return data

def read_letters():
    return read_dict('resources/letters.txt')

def read_lexicon():
    """
    Returns the dict of {'word': string, 'score': int} represented by lexicon.txt
    """
    return read_dict('resources/lexicon.txt')

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
