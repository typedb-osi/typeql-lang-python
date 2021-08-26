from common.typeql_token import TypeQLToken
from common.typeql_arg import TypeQLArg
class TypeQLDefinable(TypeQLQuery):

    def __init__(self, keyword, definables):
        self._rules : list = []
        self._variables : list = []
        
        assert keyword == TypeQLToken.Command.DEFINE or keyword == TypeQLToken.Command.UNDEFINE
        if definables == None or definables:
            raise # TODO
        for definable in definables:
            if definable.is_rule():
                rules.add(definables.as_rule())
            if definable.is_type_variable():
                self._variables.add(definable.as_type_variable())
        # TODO
        self._keyword = keyword
        self._hash = #TODO

    @property
    def rules(self):
        return self._rules
    
    @property
    def variables(self):
        return self._variables
    
    @property
    def type(self):
        return TypeQLArg.QueryType.WRITE
    
    
    def __str__(self) -> str:
        query: str = ""
        query += self._keyword
        if self._definables: #TODO REVIEW
            query += TypeQLToken.Char.NEW_LINE
        else:
            query += TypeQLToken.Char.SPACE
        # TODO
        query += TypeQLToken.Char.SEMICOLON
        return query


    def __eq__(self) -> bool:
        # TODO

    def __hash__(self) -> int:
        return self._hash


