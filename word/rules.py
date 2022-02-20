"""
Rules
"""


def matches(rules, word):
    """
    Checks if all the rules match a word
    """
    for rule in rules:
        if not rule.eval(word):
            return False
    return True


Y = 'Y'
B = 'B'
G = 'G'


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

    def __str__(self):
        positions = ['first', 'second', 'third', 'fourth', 'fifth']
        h = 'has' if self._has else 'does not have'
        color = self._color()
        at_colored = 'somewhere' if color == Y else 'anywhere'
        at = at_colored if self._pos is None else f'in the {positions[self._pos]} position'
        return f'[{color}] The word {h} "{self._letter}" {at}.'

    def _color(self):
        if not self._has:
            if self._pos is None:
                return B
            else:
                return Y
        else:
            if self._pos is None:
                return Y
            else:
                return G

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
            if self._pos is None:
                return self._letter not in word
            else:
                return word[self._pos] != self._letter
        if self._pos is None:
            return self._letter in word
        return word[self._pos] == self._letter


class RuleBuilder:
    """
    Build rules lexicallly from results, e.g.

    builder = RuleBuilder()
    builder.append('AEROS', f'{B}{B}{Y}{G}{G}')
    rules = builder.build()
    """

    def __init__(self):
        self._rules_by_letter = {}

    def _add_rule(self, letter, rule):
        if letter not in self._rules_by_letter:
            self._rules_by_letter[letter] = []
        self._rules_by_letter[letter].append(rule)

    def _clean_rules(self, letter):
        if letter not in self._rules_by_letter:
            return
        rules_by_color = {
            B: [],
            Y: [],
            G: []
        }
        rules = self._rules_by_letter[letter]
        for rule in rules:
            rules_by_color[rule._color()].append(rule)
        # Colored rules trump black, because blacks can apply to a second instance of a letter:
        if B in rules_by_color and (Y in rules_by_color or G in rules_by_color):
            self._rules_by_letter[letter] = []
            for rule in rules_by_color[Y]:
                self._add_rule(letter, rule)
            for rule in rules_by_color[G]:
                self._add_rule(letter, rule)

    def _add_black(self, letter):
        if letter not in self._rules_by_letter:
            rule = Rule().does_not_have(letter)
            self._add_rule(letter, rule)

    def _add_green(self, letter, position):
        rule = Rule().has(letter).at(position)
        self._add_rule(letter, rule)
        self._clean_rules(letter)

    def _add_yellow(self, letter, position):
        has_rule = Rule().has(letter).anywhere()
        not_at_rule = Rule().does_not_have(letter).at(position)
        self._add_rule(letter, has_rule)
        self._add_rule(letter, not_at_rule)
        self._clean_rules(letter)

    def append(self, word, colors):
        """
        Append rules based on word results.
        """
        if len(word) != len(colors):
            print("Nothing added, can not map {colors} onto {word}")
            return self
        print(f"Adding result: {word}/{colors}")
        for i in range(0, len(word)):
            letter = word[i]
            color = colors[i]
            if color == Y:
                self._add_yellow(letter, i)
            if color == B:
                self._add_black(letter)
            if color == G:
                self._add_green(letter, i)
        return self

    def build(self):
        """
        Return all the rules.
        """
        exploded = []
        for rules in self._rules_by_letter.values():
            for rule in rules:
                exploded.append(rule)
        return exploded
