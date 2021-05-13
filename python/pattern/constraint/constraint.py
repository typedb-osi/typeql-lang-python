class Constraint(BoundVariable):
    def variables(self):
        pass

    def is_concept(self) -> bool:
        return False

    def is_type(self) -> bool:
        return False

    def is_thing(self) -> bool:
        return False

    def as_concept(self):
        raise  # TODO

    def as_type(self):
        raise  # TODO

    def as_thing(self):
        raise  # TODO~

    def __str__(self):
        pass
