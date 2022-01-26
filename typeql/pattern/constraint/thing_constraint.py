
class ThingConstraint(ThingConstraintT):
    
    def is_thing(self) -> bool:
        return True

    def as_thing(self) -> 'ThingConstraint':
        return self

    def is_iid(self) -> bool:
        return False
    
    def is_isa(self) -> bool:
        return False
    
    def is_value(self) -> bool:
        return False
        
    def is_relation(self) -> bool:
        return False
    
    def is_has(self) -> bool:
        return False
    
    def as_iid(self):
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            IID.__class__.__name__
        )
    
    def as_isa(self):
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            Isa.__class__.__name__
        )
    
    def as_value(self):
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            Value.__class__.__name__
        )
    
    def as_relation(self):
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            Relation.__class__.__name__
        )
    
    def as_has(self):
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            Has.__class__.__name__
        )
    
class IID(ThingConstraint):

    def __init__(self, iid):
        self._regex = re.compile('0x[0-9a-f]+')
        if iid == None:
            raise TypeError
        self._iid = iid
    
    @property
    def iid(self) -> str:
        return self._iid
    
    def is_iid(self) -> bool:
        return True
    
    def as_iid(self) -> 'IID':
        return self
    
    #def __str__(self):
    #def __eq__(self):
    #def __hash__(self):
  

class Isa(ThingConstraint):

    self._type: ThingVariable 
    self._is_explicit : bool
    self._is_derived : bool


    @dispatch(str, bool)
    def __init__(self, type: str , is_explicit: bool):
    
    @dispatch(UnboundVariable, bool)
    def __init__(self, type_var: UnboundVariable, is_explicit: bool):
    
    @dispatch(Union[str, UnboundVariable], bool)
    def __init__(self, type_arg, is_explicit: bool):


    @dispatch(TypeVariable, bool, bool)
    def __init__(self, type_arg,  is_explicit: bool, is_derived: bool):

    @property
    def type(self) -> ThingVariable:
        return self._type
    
    def is_explicit(self) -> bool:
        return self._is_explicit
    
    def is_derived(self) -> bool:
        return self._is_derived
    

    #def variables(self):
    
    def is_isa(self) -> bool:
        return True
    
    def as_isa(self) -> 'Isa':
        return self

    #def __str__() -> str:
    #def __eq__() -> bool:
    #def __hash__():
    

class Relation(ThingConstraint):

    self._repetitions
    self._players: List[RolePlayer]
    self._scope: str

    @dispatch(RolePlayer)
    def __init__(self, player):

    @dispatch(List[RolePlayer])
    def __init__(self, player):
    
    def _register_players(self, players):
        for player in players:
            #TODO

    def _increment_repetition(self, player):
    
    def set_scope(self, relation_label: str):
        self._scope = relation_label
        for player in player:
            #TODO
    
    #def add_players(self, relation_label: str):
        #TODO
    
    @property
    def player(self):
        return self._players

    #def variables(self):
    
    def is_relation(self) -> bool:
        return True
    
    def as_relation(self):
        return self
    
    #def __str__(self)
    #def __eq__(self)
    #def __hash__(self)

class RolePlayer(self):

    def __init__(self):
        self._role_type: TypeVariable
        self._players: ThingVariable
        self._repetitions : int

    def role_type(self):
        return Optional.ofNullable(r)


class Has(ThingConstraint):
        _type: TypeVariable
        _attribute: ThingVariable

        @dispatch(str, ThingConstraint.Value)
        def __init__(self, type: str, value: ThingConstraint.Value):

       
        @dispatch(str, UnboundVariable)
        def __init__(self, type: str, var: UnboundVariable):

        @dispatch(UnboundVariable)
        def __init__(self, var: UnboundVariable):
        
        @property
        def attribute(self):
            return self._attribute

        @property
        def type(self):
            return self._type
        
        def is_has(self) -> bool:
            return True
        
        def as_has(self) -> 'Has':
            return self

        #def __eq__
        #def __str__
        #def __hash__

class Value(ThingConstraint):

    def __init__(self, predicate, value):
        self._predicate
        self._value 
        
    def is_value(self) -> bool:
        return True

    def as_value(self) -> 'Value':
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
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            Long.__class__.__name__
        )
    

    def as_double(self):
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            Double.__class__.__name__
        )
    
    def as_boolean(self):
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            Boolean.__class__.__name__
        )

    def as_string(self):
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            String.__class__.__name__
        )

    def as_datetime(self):
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            DateTime.__class__.__name__
        )

    def as_variable(self):
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            Variable.__class__.__name__
        )

    def __str__(self) -> str:

    def __eq__(self, other) -> bool:
        
    def __hash__(self):


class Long(Value):

    def __init__(self, predicate, value):
        super().__init__(predicate, value)

    def is_long(self) -> bool:
            return True

    def as_long(self) -> 'Long':
            return self

class Double(Value):

    def __init__(self, predicate, value):
        super().__init__(predicate, value)

    def is_double(self) -> bool:
        return True
        
    def as_double(self) -> 'Double':
        return self

class Boolean(Value):

    def __init__(self, predicate, value):
        super().__init__(predicate, value)
    
    def is_double(self) -> bool:
        return True

    def as_boolean(self) -> 'Boolean':
        return self

class String(Value):

    def __init__(self, predicate, value):
        super().__init__(predicate, value)

    def is_string(self) -> bool:
        return True    

    def as_string(self) -> 'String':
        return self

class DateTime(Value):

    def __init__(self, predicate, value):
        super().__init__(predicate, value)
        
    def is_datetime(self) -> bool:
        return True
        
    def as_datetime(self) -> 'DateTime':
        return self


class Variable(Value):

    def __init__(self, predicate, value):
        super().__init__(predicate, value)

    def variables():
        pass
        
    def is_variable(self) -> bool:
        return True
    
    def as_variable(self) - 'Variable':
        return self
