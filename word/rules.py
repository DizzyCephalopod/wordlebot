"""
Rules
"""

def matches(rules, word):
    for rule in rules:
        if not rule.eval(word):
            return False
    return True

class Rule:
    """
    Represents a rule for matching qualifying rules. Built using a fluent syntx:

    Rule.word()
        .has('A')
        .anywhere()

    Rule.word()
        .does_not_have('A')

    Rule.word()
        .has('A')
        .nowhere()

    Rule.word()
        .has('A')
        .at(3)
    """

    def __init__(self):
        self._has = True
        self._letter = None
        self._pos = None

    @staticmethod
    def word():
        """
        Start building a word rule
        """
        return Rule()

    def has(self, letter):
        """
        Explain which letter this is about.
        """
        self._letter = letter
        self._has = True
        return self

    def does_not_have(self, letter):
        """
        This rule is about a letter we know is missing.
        """
        self._letter = letter
        self._has = False
        return self

    def at(self, pos=None):
        """
        Explain more about the position of the letter.
        """
        self._pos = pos
        return self

    def anywhere(self):
        """
        Explain that this letter can be anywhere.
        """
        return self.at()

    def nowhere(self):
        """
        Explain that this letter is certainly missing.
        """
        self.at()
        self._has = False
        return self

    def eval(self, word):
        """
        Returns true if this word matches the rule, otherwise False.
        """
        if not self._has:
            return self._letter not in word
        if self._pos is None:
            return self._letter in word
        return word[self._pos] == self._letter
