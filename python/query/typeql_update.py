from query.typeql_writable import TypeQLWritable
from common.typeql_token import TypeQLToken

class TypeQLUpdate(TypeQLWritable):

    def __int__(self, match, delete_variables, insert_variables):
        self._delete_variables
        self._insert_variables
        self._hash
        self._named_delete_variables_unbound
        self._insert_delete_variables_unbound
        
        assert(match) != None
        self._match #TODO


    @property
    def match(self):
        return self._match
        
    @property
    def delete_variables(self):
        return self._delete_variables

    @property
    def insert_variables(self):
        return self._insert_variables

    @property
    def named_delete_variables_unbound(self):
        if self._named_delete_variables_unbound == None:
            pass #TODO
    
    @property
    def named_insert_variables_unbound(self):
        if self._named_insert_variables_unbound == None:
            pass #TODO
    
    def __str__(self):
        query: str = ""
        query += self._match + TypeQLToken.Char.NEW_LINE
        query += TypeQLToken.Command.DELETE
        if len(self._delete_variables) > 1:
            query += TypeQLToken.Char.NEW_LINE
        else:
            query += TypeQLToken.Char.SPACE
        # TODO
        query += TypeQLToken.Char.SEMICOLON
        return query

    def __eq__(self):
        pass

    def __hash__(self):
        pass