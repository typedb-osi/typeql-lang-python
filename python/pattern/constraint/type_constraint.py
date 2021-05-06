
class TypeConstraint(Constraint):

    def variables(self):
        pass
    
    def is_type(self) -> bool:
        return True
    
    def as_type(self):
        return self
    
    def is_label(self) -> bool:
        return False
    
    def is_sub(self) -> bool:
        return False
    
    def is_abstract(self) -> bool:
        return False

    def is_value_type(self) -> bool:
        return False
    
    def is_regex(self) -> bool:
        return False
    
    def is_owns(self) -> bool:
        return False
    
    def is_plays(self) -> bool:
        return False
    
    def is_plays(self) -> bool:
        return False
    
    def is_relates(self) -> bool:
        return False
    
    def as_label(self):
        raise 
    
    def as_sub(self):
        raise
    
    def as_abstract(self):
        raise
    
    def as_value_type(self):
        raise
    
    def as_regex(self):
        raise
    
    def as_owns(self):
        raise
    
    def as_plays(self):
        raise
    
    def as_relates(self):
        raise


class Label(TypeConstraint):

    def __init__(self, scope, label):
        self._scope = scope
        self._label = label
    
    @property
    def scope(self):
        pass
    
    @property
    def label(self):
        return self._label
    
    def scoped_label(self):
        pass
    
    def is_label(self) -> bool:
        return True
    
    def as_label(self):
        return self
    
    def __str__(self):
        return TYPE.__str__() + SPACE + self.scoped_label()
    
    def __eq__(self, other):
        pass  # TODO
    
    def __hash__(self):
        return # TODO
    

class Sub(TypeConstraint):

    def __init__(self, type, typeVar, typeScope, typeLabel, isExplicit):

    @property
    def type(self):
        return self._type
    
    def is_explicit(self):
        return self._isExplicit
    
    def variables(self):
        pass
    
    def is_sub(self) -> bool:
        return True
    
    def as_sub(self):
        return self
    
    def __str__(self):
        pass
    
    def __eq__(self, other):
        pass  # TODO
    
    def __hash__(self):
        return # TODO

class  Abstract(TypeConstraint):
    def is_abstract(self) -> bool:
        return True
    
    def as_abstract(self):
        return self
    
    def __str__(self):
        pass
    
    def __eq__(self, other):
        pass  # TODO
    
    def __hash__(self):
        pass # TODO


class ValueType(TypeConstraint):

    def __init__(self, valueType):
        self._valueType = valueType
    
    @property
    def value_type(self):
        self._valueType
    
    def is_value_type(self) -> bool:
        return True
    
    def as_value_type(self):
        return self
    
    def __str__(self):
        pass
    
    def __eq__(self, other):
        pass  # TODO
    
    def __hash__(self):
        pass # TODO

class Regex(TypeConstraint):
    
    def __init__(self, regex):
        try:
            self._regex = regex # TODO

    @property
    def regex(self):
        return self._regex
    
    def is_regex(self) -> bool:
        return True
    
    def as_regex(self):
        return self

    def __str__(self):
        pass # TODO
    
    def __eq__(self, other):
        pass  # TODO
    
    def __hash__(self):
        pass # TODO


class Owns(TypeConstraint):

    def __init(self, attributeTypeVar,  attributeTypeArg, overriddenAttributeType, attributeType, isKey)
        pass # TODO
    
    @property
    def attribute(self):
        return self._attribute
    
    @property
    def overridden(self):
        return self._overridden
    
    @property
    def is_key(self):
        return self._isKey
    

    def variables(self):
        pass
    
    def is_owns(self) -> bool:
        return True
    
    def as_owns(self):
        return self
    
    def __str__(self):
        pass # TODO
    
    def __eq__(self, other):
        pass  # TODO
    
    def __hash__(self):
        pass # TODO


class Plays(TypeConstraint):
    
    def __init__(self, relationType, roleTypeVar, roleTypeArg, roleType, var, overriddenRoleType, overriddenRoleTypeVar, overriddenRoleTypeArg)


    def variables(self):
        pass #TODO
    
    def is_plays(self) -> bool:
        return True
    
    def as_plays(self):
        return self
        
    def __str__(self):
        pass # TODO
    
    def __eq__(self, other):
        pass  # TODO
    
    def __hash__(self):
        pass # TODO

class Relates(TypeConstraint):

    def __init__(self, roleType, roleTypeVar, roleTypeArg, overriddenRoleType, overriddenRoleTypeVar, overriddenRoleTypeArg):

    @property
    def scoped_type(self):
    
    @scoped_type.setter
    def scoped_type(self):
    
    @property
    def role(self):
        return self._roleType
    
    @property
    def overridden(self):
        pass # TODO

    @property
    def variables(self):
        return self._roleType
    
    def is_relates(self):
        return True
    
    def as_relates(self):
        return self
    
    def __str__(self):
        pass # TODO
    
    def __eq__(self, other):
        pass  # TODO
    
    def __hash__(self):
        pass # TODO