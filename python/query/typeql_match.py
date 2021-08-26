

from typing import Optional
from common.typeql_token import TypeQLToken
from common.typeql_arg import TypeQLArg

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
            syntax: str = ""
            if not self._filter == None:
                syntax += TypeQLToken.Filter.GET
                #TODO
                syntax += TypeQLToken.Char.SPACE  #+ TODO
                syntax += TypeQLToken.Char.SEMICOLON


        def __eq__(self):
            pass

        def __hash__(self):
            pass
    
    class Unfilter():
        def __init__(self, patterns):
            pass
        
        def valid_conjunction(self, patterns):
            if len(patterns) == 0:
                raise #TODO
            return #TODO 
        
        def get(self,):
            pass #TODO
        def sort(self, sorting):
            pass #TODO
        def offset(self, offset):
            pass #TODO
        def limit(self, limit):
            pass #TODO
        def insert(self,):
            pass #TODO
        def delete(self,):
            pass #TODO
        
    class Filtered():
        def __init__(self, unfiltered, filter):
            pass

        def sort(self, sorting):
            pass
        
        def offset(self, offset):
            pass

        def limit(self, limit):
            pass
    
    class Stored():

        def __init__(self, match, sorting):
            pass 
        
        def offset(self, offset):
            pass
        
        def limit(self, limit):
            pass
    
    class Offset():

        def __init__(self, match, offset):
            pass

        def limit(self, limit):
            pass

    class Limited():
        def __init__(self, match, limit):
            pass
    
    class Aggregate():
        def __init__(self, query, method, var):
            self._query
            self._method
            self._var
            self._hash
            if query == None:
                raise
            if method == None:
                raise 
            if var == None and (not method.equals(TypeQLToken.Aggregate.Method.COUNT)):
                raise

            self._query = query
            self._method = method
            self._var = var
            self._hash = #TODO

        def type(self):
            return TypeQLArg.QueryType.READ

        @property
        def match(self):
            return self._query

        @property
        def method(self):
            return self._method
        
        @property
        def var(self):
            return self._var
        
        def __str__(self):
            query: str = ""
            query += TypeQLToken.Char.NEW_LINE
             
        def __eq__(self):
            pass

        def __hash__(self):
            pass 
    

    class Group():
        def __init__(self, query, var):
            if query == None:
                raise # TODO
            if var == None:
                raise # TODO
            
            self._query = query
            self._var = var
            self._hash = #TODO

        @property
        def type(self):
            return TypeQLArg.QueryType.READ

        @property
        def match(self):
            return self._query
        
        @property
        def var(self):
            return self._var
        
        def aggregate(self, method, var):
            pass #TODO

        def __str__(self) -> str:
            query: str = ""
            pass 

    class Aggregate():
        
        def __init__(self, group, method, var):
            if group == None:
                raise 
            if method == None:
                raise
            if var == None #TODO:
                raise
            self._group = group
            self._method = method
            self._var = var
            self._hash = #TODO

        @property
        def type(self):
            return TypeQLArg.QueryType.READ
        
        @property
        def group(self):
            return self._group
        
        @property
        def method(self):
            return self._method
        
        def __str__(self) -> str:
            pass

        def __eq__(self, o: object) -> bool:
            pass

        def __hash__(self) -> int:
            pass
