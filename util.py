"""
#Common Utilities
Utilities used throughout the rest of the app.
"""

def print_list(arr):
    """ Prints a list one item per line
    """
    for i in arr:
        print(i)


def print_scores(scores):
    """ Prints a list of scores.
    A score is in the format {'word': string, 'score': int}
    """
    for score in scores:
        print(f"{score['word']}|{score['score']}")

def read_file(filename):
    """ Reads all the lines in a file.
    """
    with open(filename, encoding='utf-8') as f:
        lines = []
        for line in f:
            lines.append(line.strip())
        return lines
