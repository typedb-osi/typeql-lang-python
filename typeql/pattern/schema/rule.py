from multipledispatch import dispatch



class Rule(Definable):

    @dispatch(str)
    def __init__(self, label):
        self.label = label
    
    @dispatch(str, Conjunction, ThingVariable)
    def __init__(self, label, when, variable):
        self._label = label
        self._when = when
        self._then = variable

    def is_rule(self):
        return True

    def as_rule(self):
        return self

    @property
    def label(self) -> str:
        return self._label
    
    @dispatch(None)
    @property
    def when(self):
        return self._when
    
    @dispatch(Conjunction)
    @property
    def when(self)-> IncompleteRule:
        return  IncompleteRule(self._label, self._when)

    @property
    def then(self) -> ThingVariable:
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