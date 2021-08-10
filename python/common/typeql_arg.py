from enum import Enum, EnumMeta

class TypeQLArg():
    
    class QueryType(Enum, metaclass=TypeQLArg):
        READ = 0
        WRITE = 1
        
        def __init__(self, id):
            self.id
            self.is_write
            super().__init__(self)
       
        def of(self, value : int):
            pass
        
        @staticmethod
        def is_read(self):
            return not self.is_write
        
        @staticmethod
        def is_write(self):
            return self.is_write


    class ValueType():
        BOOLEAN = "boolean"
        DATETIME = "datetime"
        DOUBLE = "double"
        LONG = "long"
        STRING = "string"
        

    class Order(Enum):
        ASC = "asc"
        DESC = "desc"


    class Algorithm(Enum):
        DEGREE = "degree"
        K_CORE = "k_core"
        CONNECTED_COMPONENT = "connected-component"


           
            