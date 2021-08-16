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
        super(match)
        assert keyword == TypeQLArg.QueryType.INSERT or keyword == TypeQLArg.QueryType.DELETE
        if variables == None or variables.is_empty():
            raise # TODO
        self._keyword = keyword
        self._variables = variables
        self._hash = hash(self._keyword, self._variables)

    def __str__(self):


    def __eq__(self) -> bool:


    def __hash__(self):
        return hash()