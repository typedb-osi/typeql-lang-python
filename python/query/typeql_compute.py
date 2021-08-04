
class TypeQLCompute(TypeQLQuery):

    def __init__(self):
        self _method
        self.include_attributes : bool
        self.from_id : str = None
        self.to_id : str = None
        self.of_types : str = None
        self.in_types : str = None
        self.algorithm = None
        self.arguments = None

    
    def _in(self):
    def includes_attributes(self):
    
    @property
    def query_type(self):
        return QueryType.WRITE

    @property
    def method(self):
        return self.method
    
    @property
    def includes_attributes(self):
        return self.includes_attributes
    

    def is_valid(self):
        # TODO IMPLEMENTATION
        pass
    
    def _print_conditions(self):
        # TODO IMPLEMENTATION
        pass

    def _print_of(self):
    def _print_in(self):
    def _print_types(self):
    def _print_algorithm(self):
    def _print_arguments(self):
    def __str__(self):


class Builder():
    def count_(self):
    def max_(self):
    def min_(self):
    def mean_(self):
    def median_(self):
    def sum_(self):
    def std_(self):
    def centrality_(self):
    def cluster_(self):
    
class Statistics():
    def as_count(self):
    def as_value(self):

class Count():
    def inside(self):
    def attributes(self):
    def conditions_required(self):
    @property
    def exception(self):
    def __eq__(self):
    def __hash__(self):


class Value():
    def __init__(self):
    def of(self, types: str):
    def inside(self, types: str):
    def attributes(self, include: bool):
    def conditions_required(self):
    def exception(self):
    def __eq__(self)
    
class Path():
    def __init__(self):
    def from_(self):
    def to_(self):
    def in_(self):
    def attributes_(self):
    def conditions_required(self):
    @property
    def exception(self):
    def __eq__(self):
    def __hash__(self):


class Centrality():
    
    def __init__(self):
    
    @property
    def self(self):
        return self
    
    def of_(self):
    
    def algorithms_accepted(self):
    
    def arguments_accepted(self):
    
    def arguments_default(self):
    def __eq__(self):
    def __hash__(self):
        

class Cluster():
    def __init__(self):
        
class Arguments():
    def __init__(self):
        self._arguments_ordered 
        self._defaults
        self._arguments_map
        self._arguments 

    @property
    def argument(self, param):
        return self._arguments_map.get(param).get()
    
    @argument.setter
    def argument(self, arg):
        self._arguments_ordered.remove(arg.type())
        self._arguments_ordered.put(arg.type(), arg)
    
    def _set_defaults(self, defaults):
        self._defaults = defaults
    
    @property
    def parameters(self):
        return self._arguments_ordered.key_set ???

    def min_K(self):
    
    def k(self):
    
    def size(self):

    def constains(self):

    @property
    def  _argument_value(self):
    
    def __eq__(self):
    
    def __hash__(self):