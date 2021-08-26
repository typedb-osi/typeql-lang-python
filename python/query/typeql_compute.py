from query.builder.computable import Computable
from common.typeql_token import TypeQLToken
from common.typeql_arg import TypeQLArg
class TypeQLCompute(Computable):

    def __init__(self, method, include_attributes):
        self._method = method
        self._include_attributes : bool = include_attributes
        self._from_id : str = None
        self._to_id : str = None
        self._of_types : str = None
        self._in_types : str = None
        self._algorithm = None
        self._arguments = None


    @property
    def type(self):
        return TypeQLArg.QueryType.WRITE

    @property
    def method(self):
        return self._method

    @property
    def in_(self):
        if self.in_types == None:
            return 
        else: 
            return self._in_types


    @property
    def includes_attributes(self):
        return self._include_attributes
    
    @property
    def query_type(self):
        return TypeQLArg.QueryType.WRITE

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
        conditions: list = []
        if self._from_id != None:
            conditions.append(TypeQLToken.Compute.Condition.FROM + TypeQLToken.Char.SPACE + self._from_id)
        if self._to_id != None:
            conditions.append(TypeQLToken.Compute.Condition.TO + TypeQLToken.Char.SPACE + self._to_id)
        if self._of_types != None:
            conditions.append(self._print_of())
        if self._in_types != None:
            conditions.append(self._print_in())
        if self._algorithm != None:
            conditions.append(self._print_algorithm())
        if self._arguments != None and not self._arguments.get_parameters().is_empty():
            conditions.append(self._print_arguments())

        return TypeQLToken.Char.COMMA_SPACE.join(conditions)

    def _print_of(self) -> str:
        if self._of_types != None:
            return TypeQLToken.Compute.Condition.OF + TypeQLToken.Char.SPACE + self.print_types(self._of_types)
        else:
            return ""
    
    def _print_in(self) -> str:
        if self._in_types != None:
            return TypeQLToken.Compute.Condition.IN + TypeQLToken.Char.SPACE + self.print_types(self._in_types)

    def _print_types(self, types):
        in_types: str = ""
        pass #TODO

    def _print_algorithm(self):
        if self._algorithm != None:
            return TypeQLToken.Compute.Condition.USING + TypeQLToken.Char.SPACE + self._algorithm
        else:
            return ""
        
    def _print_arguments(self):
        if self._arguments == None:
            return ""
        else:
            arguments_list: list = []
            arguments_string: str = ""
            for param in self._arguments.get_parameters():
               # arguments_list.append(param + TypeQLToken.Predicate.Equality.EQ + )
                pass #TODO
            if not arguments_list.is_empty():
                arguments_string += TypeQLToken.Compute.Condition.WHERE + TypeQLToken.Char.SPACE
                if len(arguments_list) == 1:
                    arguments_string  += arguments_list[0]
                else:
                    arguments_string += TypeQLToken.Char.SQUARE_OPEN
                    arguments_string += TypeQLToken.Char.COMMA_SPACE.join(arguments_list)
                    arguments_string += TypeQLToken.Char.SQUARE_CLOSE
        return arguments_string

    def __str__(self) -> str:
        query: str = ""
        query += TypeQLToken.Command.COMPUTE + TypeQLToken.Char.SPACE + self._method
        if not self.print_conditions.is_empty:
            query += TypeQLToken.Char.SPACE + self.print_conditions()
        query += TypeQLToken.Char.SEMICOLON
        return query

    class Builder():

        def count(self):
            return TypeQLCompute.Statistics.Count()

        def max(self):
            return TypeQLCompute.Statistics.Value(TypeQLToken.Compute.Method.MAX)

        def min(self):
            return TypeQLCompute.Statistics.Value(TypeQLToken.Compute.Method.MIN)

        def mean(self):
            return TypeQLCompute.Statistics.Value(TypeQLToken.Compute.Method.MEAN)

        def median(self):
            return TypeQLCompute.Statistics.Value(TypeQLToken.Compute.Method.MEDIAN)

        def sum(self):
            return TypeQLCompute.Statistics.Value(TypeQLToken.Compute.Method.SUM)

        def std(self):
            return TypeQLCompute.Statistics.Value(TypeQLToken.Compute.Method.STD)

        def path(self):
            return TypeQLCompute.Path()

        def centrality(self):
            return TypeQLCompute.Centrality()

        def cluster(self):
            return TypeQLCompute.Cluster()
        
    class Statistics():
        def __init__(self, method, include_attributes):
            self._method = method
            self._include_attributes = include_attributes

        def as_count(self):
            if isinstance(self, TypeQLCompute.Statics.Count):
                return self
            else:
                pass
                # TODO raise TypeQLException
        
        def as_value(self):
            if isinstance(self, TypeQLCompute.Statistics.Value):
                return self
            else:
                pass
                # TODO raise TypeQLException
    class Count(TypeQLCompute.Statistics):
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
        return self._arguments_ordered.key_set

    def min_K(self):
    
    def k(self):
    
    def size(self):

    def constains(self):

    @property
    def  _argument_value(self):
    
    def __eq__(self):
    
    def __hash__(self):
