
from common.exception.typeql_exception import TypeQLException
from common.typeql_token import TypeQLToken
from query.typeql_writable import TypeQLWritable
class TypeQLInsert(TypeQLWritable.InsertOrDelete):



    def __init__(self, match, variables):
        #super(TypeQLToken.Command.INSERT, match, #TO SET)
        self._match = match



    def validate_insert_vars(self, match, variables):
        if match != None:
            #TODO 
            pass
        return variables

    @property
    def variables(self):
        return self._variables 
    
    @property
    def match(self):
        return self.__match