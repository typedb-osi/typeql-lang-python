from query.typeql_query import TypeQLQuery
from common.typeql_arg import TypeQLArg
from common.typeql_token import TypeQLToken
class TypeQLWritable(TypeQLQuery):
    def __init__(self, match):
        self._match = match
    
    def type(self):
        return TypeQLArg.QueryType.WRITE
    

class InsertOrDelete(TypeQLWritable):
    def __init__(self, keyword, match, variables):
        #super(match)
        assert keyword == TypeQLArg.QueryType.INSERT or keyword == TypeQLArg.QueryType.DELETE
        if variables == None or variables.is_empty():
            raise # TODO
        self._variables = variables
        self._keyword = keyword
        self._variables = variables
        self._hash = hash(self._keyword, self._variables)

    def __str__(self):
        query: str = ""
        if self._match != None:
            query += self._match + TypeQLToken.Char.NEW_LINE
        query += self._keyword
        if len(self._variables) > 1:
            query += TypeQLToken.Char.NEW_LINE
        else:
            query += TypeQLToken.Char.SPACE
        
        # TODO
        query += TypeQLToken.Char.SEMICOLON
        return query

    def __eq__(self) -> bool:
        pass


    def __hash__(self):
        return hash()