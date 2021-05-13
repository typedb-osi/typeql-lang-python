from abc import ABC, abstractmethod


class Conjunctable(IPattern):
    @abstractmethod
    def is_conjuctable(self) -> bool:
        return True

    @abstractmethod
    def as_conjuctable(self):
        return self
