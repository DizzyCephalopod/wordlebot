from statistics.popularity import score_all
from util import read_file, print_scores

if __name__ == '__main__':
    words = read_file('resources/words.txt')
    scores = score_all(words)
    print_scores(scores)
