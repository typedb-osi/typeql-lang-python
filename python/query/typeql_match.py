

from typing import Optional


class TypeQLMatch():
    #TODO dispatcher
    def __int__(self, conjunction, filter):
        self._conjunction
        self._modifiers
        self._hash
        self._variables
        self._variables_named_unbound
    

    class Modifiers():
        def __init__(self):
            self._filter
            self._sorting
            self._offset
            self._limit
            self._hash
        
        @property
        def filter(self):
            pass

        @property
        def offset(self):
            pass
        
        @property
        def limit(self):
            pass

        @property
        def sort(self):
            pass

        def is_empty(self):
            pass

        def __str__(self):
            pass

        def __eq__(self):
            pass

        def __hash__(self):
            pass