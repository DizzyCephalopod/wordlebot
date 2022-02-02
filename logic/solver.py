"""
Defines a strategy for solving a complete puzzle.
"""

class Config:
    """
    Defines configuration for solving a wordle.
    """
    def __init__(self):
        pass

    @property
    def elimination_threshhold(self):
        return self._elimination_threshhold

    @property.setter
    def elimination_threshhold(self, threshhold):
        self._elimination_threshhold = threshhold

class State:
    def __init__(self, config):
        self._state = []
        self._config = config

    @property
    def num_green(vowels=None): # None, true, false
        return 0

    @property
    def num_yellow(vowels=None): # None, true, false
        return 0

class Solver:
    """
    Solves a wordle
    """
    def __init__(self, lexicon):
        self._lexicon = lexicon
        self._possible = lexicon
        self._state = []

    def make_guess(self, strategy, guess_number):
        if guess_number == 1:
            return 'AEROS'
        # example: determine strategy based on things:
        if self._state.num_yellow > 3:
            return '' # eliminate
        # default:
        return ''

    def solve(self, word):
        """
        This is currently a backtest solve. 
        """
        strategy = "elimination"
        guess_number = 0
        while True:
            guess_number += 1
            guess = self.make_guess(strategy, guess_number)
            self._state = self.apply_guess(guess)
            if self.is_solved():
                break
            if guess_number >= 6:
                break
            strategy = self.select_strategy()
        return self._state

            