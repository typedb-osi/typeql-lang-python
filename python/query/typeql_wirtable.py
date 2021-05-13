class TypeQLWritable(TypeQLQuery):
    def __init__(self, match):
        self._match = match
    
    def type(self):
        return WRITE
    

class InsertOrDelete(TypeQLWritable):
    def __init__(self, keyword, match, variables):
        super(match)
        assert keyword == INSERT or keyword == DELETE
        if variables == None or variables.is_empty():
            raise # TODO
        self._keyword = keyword
        self.variables = variables

    def __str__(self):
    def __eq__(self):
    def __hash__(self):