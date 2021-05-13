
class TypeQLDefinable(TypeQLQuery):

    def __init__(self, keyword, definables):
        self._rules : list
        self._variables : list
        self._keyword = keyword
        assert keyword == DEFINE or keyword == UNDFINE
        if definables == None or definables.is_empty():
            raise # TODO
        for definable in definables:
            if definable.is_rule():
                rules.add(definables.as_rule())
            if definable.is_type_variable():
                self._variables.add(definable.as_type_variable())
        # TODO

    @property
    def rules(self):
        return self._rules
    
    @property
    def variables(self):
        return self._variables
    
    
    def type(self):
        return TypeQLArg.QueryType.WRITE
    
    
    def __str__(self):
        # TODO
    def __eq__(self):
        # TODO
    def __hash__(self):
        # TODO


