
from typing import List
from typeql_python.pattern.pattern import IPattern
from typeql_python.types.pattern import PatternT


class Conjunction(IPattern):
    patterns : List
    hash: int
    normalised
    
    def __init__(self, patterns) -> None:
        self._patterns
        self._hash
        self._normalised


        