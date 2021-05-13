class Rule(Definable):
    def __init__(self, label, when, variable):
        self._label = label
        self._when = when
        self._then = variable

    def is_rule(self):
        return True

    def as_rule(self):
        return self

    @property
    def label(self):
        return self._label

    @property
    def when(self):
        # IncompleteRule(label, when);
        return self._when

    @property
    def then(self):
        # IncompleteRule(label, when);
        return self._then

    def validate(self, label, when, then):
        pass  # TODO

    def validate_when(self, label, when):
        pass  # TODO

    def find_negations(self, pattern):
        pass  # TODO

    def find_disjunctions(self, pattern):
        pass  # TODO

    def __str__(self):
        pass  # TODO

    def __eq__(self, other):
        pass  # TODO

    def __hash__(self):
        pass  # TODO


class IncompleteRule:
    def __init__(self, label, when):
        self._label = label
        self._when = when

    def then(then):
        return  # TODO
