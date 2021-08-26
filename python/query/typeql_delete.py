from query.typeql_writable import TypeQLWritable
from common.typeql_token import TypeQLToken
class TypeQLDelete(TypeQLWritable.InsertOrDelete):
    def __init__(self, match, variables):
        pass
    
    def valid_delete_vars(self, match, variables):
        for var in variables:
            #TODO
            pass
        return variables

    
    @property
    def match(self):
        pass
    
    @property
    def variables(self):
        return self._variables
    
    def insert(self, things):
        #TODO
        pass
