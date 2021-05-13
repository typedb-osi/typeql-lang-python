from abc import ABC, abstractmethod


class Definable(ABC):
    def is_rule(self):
        return False

    def is_type_variable(self):
        return False

    def as_rule(self):
        raise  # TODO

    def as_type_variable(self):
        raise  # TODO
