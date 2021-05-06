
class ThingConstraint(Constraint):

    def is_thing(self):
        return True
    
    @property
    def as_thing(self) -> ThingConstraint:
        return self
    
    def is_iid(self):
        return False
    
    def is_isa(self):
        return False
    
    def is_value(self):
        return False
    
    def is_relation(self):
        return False
    
    def is_relation(self):
        return False
    
    def is_has(self):
        return False
    
    def as_iid(self):
        raise 
    
    def as_isa(self):
        raise

    def as_value(self):
        raise

    def as_relation(self):
        raise

    def as_has(self):
        raise
    

class IID(ThingConstraint):

class Isa(ThingConstraint):

class Relation(ThingConstraint):

class Has(ThingConstraint):

class Value(ThingConstraint):

    def __init__(self, predicate, value):
        
    def is_value(self):
        return True

    def as_value(self):
        return self

    @property
    def predicate(self):
        return self._predicate
    
    @property
    def value(self):
        return self._value
    
    def is_long(self) -> bool:
        return False
    
    def is_double(self) -> bool:
        return False
    
    def is_string(self) -> bool:
        return False

    def is_string(self) -> bool:
        return False    

    def is_double(self) -> bool:
        return False

    def is_datetime(self) -> bool:
        return False

    def as_long(self):
    def as_double(self):
    def as_boolean(self):
    def as_string(self):
    def as_datetime(self):
    def as_variable(self):
    def __str__(self):
    def __eq__(self, other):
    def __hash__(self):


class Long(Value):

    def __init__(self, predicate, value):
        super().__init__(predicate, value)

    def is_long(self):
            return True

    def as_long(self):
            return self

class Double(Value):

    def __init__(self, predicate, value):
        super().__init__(predicate, value)

    def is_double(self) -> bool:
        return True
        
    def as_double(self):
        return self

class Boolean(Value):

    def __init__(self, predicate, value):
        super().__init__(predicate, value)
    
    def is_double(self) -> bool:
        return True

    def as_boolean(self):
        return self

class String(Value):

    def __init__(self, predicate, value):
        super().__init__(predicate, value)

    def is_string(self) -> bool:
        return True    

    def as_string(self):
        return self

class DateTime(Value):

    def __init__(self, predicate, value):
        super().__init__(predicate, value)
        
    def is_datetime(self) -> bool:
        return True
        
    def as_datetime(self):
        return self


class Variable(Value):

    def __init__(self, predicate, value):
        super().__init__(predicate, value)

    def variables():
        pass
        
    def is_variable(self) -> bool:
        return True
    
    def as_variable(self):
        return self