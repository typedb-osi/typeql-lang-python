from query.typeql_writable import TypeQLWritable

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
        pass

    def __eq__(self):
        pass

    def __hash__(self):
        pass