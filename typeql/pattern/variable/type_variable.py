from multipledispatch import dispatch

class TypeVariable():

    def __init__(self):
        self._label_constraint 
        self._sub_constraint
        self._abstract_constraint
        self._value_type_constraint
        self._regex_constraint
        self._owns_constraints : List = []
        self._play_constraints : List = []
        self._relates_constraints : List = []
        self._constraints : List = []
    
    @property
    def constraints(self):
        return self._constraints

    def is_type(self):
        return True
    
    def as_type(self):
        return self

    @dispatch(TypeConstraint.Label)
    def constrain(self, constraint):
        if self._label_constraint != None:
            #raise TypeQLException.of()
        self._label_constraint = constraint
        constraints.append(constraint)
        for rel in self._regex_constraint:
            #rel = 
        return self
    
    @dispatch(TypeConstraint.sub)
    def constrain(self, constraint):
        if self._sub_constraint != None:
             #raise TypeQLException.of()
        self._sub_constraint = constraint
        constraints.add(constraint)
        return self

    @dispatch(TypeConstraint.Abstract)
    def constrain(self, constraint):
        if self._abstract_constraint != None:
            #raise TypeQLException.of()
        self._abstract_constraint = constraint
        constraints.add(constraint)
        return self
    
    @dispatch(TypeConstraint.ValueType)
    def constrain(self, constraint):
        if self._value_type_constraint != None:
            #raise TypeQLException.of()
        self._value_type_constraint = constraint
        constraints.add(constraint)
        return self
       
    @dispatch(TypeConstraint.Regex)
    def constrain(self, constraint):
        if self._regex_constraint != None:
            #raise TypeQLException.of()
        self._regex_constraint = constraint
        constraints.add(constraint)
        return self
    
    @dispatch(TypeConstraint.Owns)
    def constrain(self, constraint):
        if self._owns_constraints != None:
            #raise TypeQLException.of()
        self._owns_constraints = constraint
        constraints.add(constraint)
        return self
    
    @dispatch(TypeConstraint.Plays)
    def constrain(self, constraint):
        if self._play_constraints != None:
            #raise TypeQLException.of()
        self._play_constraints = constraint
        constraints.add(constraint)
        return self
    
    @dispatch(TypeConstraint.Relates)
    def constrain(self, constraint):
        if self.label().is_present():
            #constraint.set_scope()
        self._relates_constraints.append(constraint)
        constraints.append(constraint)
        return self
    
    
    def label(self):
        return Optional.of_nullable(self._label_constraint)
    
    
    def sub(self):
        return Optional.of_nullable(self._sub_constraint)
    
        
    def abstract_constraint(self):
        return Optional.of_nullable(self._abstract_constraint)
    
    def value_type(self):
        return Optional.of_nullable(self._value_type_constraint)
    
    def regex(self):
        return Optional.of_nullable(regex.constraint)
    
    def owns(self):
        return self._owns_constraints
    
    def play(self):
        return self._play_constraints
    
    def relates(self):
        return self._relates_constraints
    
    #def __str__()
    #def __eq__()
    #def __hash__()
    
    def is_type_variable(self):
        return True
    
    def as_type_variable(self):
        return self