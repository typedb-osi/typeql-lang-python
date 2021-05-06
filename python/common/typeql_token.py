from __future__ import annotations
from typing import Optional
from enum import Enum, EnumMeta

class TypeQLToken:

    class Type(Enum):
        THING = "thing"
        ENTITY = "entity"
        ATTRIBUTE = "attribute"
        RELATION ="relation"
        ROLE = "role"


    class Command(Enum):
        COMPUTE = "compute"
        DEFINE = "define"
        UNDEFINE = "undefine"
        INSERT = "insert"
        DELETE = "delete"
        MATCH = "match"
        AGGREGATE = "aggregate"
        GROUP = "group"
        
        @staticmethod
        def of(
            value: str,
        ) -> Union[
            Command.COMPUTE,
            Command.DEFINE,
            Command.UNDEFINE,
            Command.INSERT,
            Command.MATCH,
            Command.AGGREGATE,
            Command.GROUP
            None,
        ]:
            for c in Command:
                if c.value == value:
                    return c
            return None


    class Filter(Enum):
        GET = "get"
        SORT = "sort"
        OFFSET = "offset"
        LIMIT = "limit"

        @staticmethod
        def of(
            value: str,
        ) -> Union[
            Filter.GET,
            Filter.SORT,
            Filter.OFFSET,
            Command.LIMIT,
            None,
        ]:
            for c in Filter:
                if c.value == value:
                    return c
            return None

    class Char(Enum):
        EQUAL = "="
        COLON = ":"
        SEMICOLON = ";"
        SPACE = " "
        COMMA = ","
        COMMA_SPACE = ", "
        CURLY_OPEN = "{"
        CURLY_CLOSE = "}"
        PARAN_OPEN = "("
        PARAN_CLOSE = ")"
        SQUARE_OPEN = "["
        SQUARE_CLOSE = "]"
        QUOTE_DOUBLE = "\""
        QUOTE_SINGLE = "'"
        NEW_LINE = "\n"
        UNDERSCORE = "_"
        VAR_  = "$_"
        VAR = "$"
        
        @staticmethod
        def of(
            value: str,
        ) -> Union[
            Char.EQUAL,
            Char.COLON,
            Char.SEMICOLON,
            Char.COMMA,
            Char.COMMA_SPACE,
            Char.CURLY_OPEN,
            Char.CURLY_CLOSE,
            Char.PARAN_OPEN,
            Char.PARAN_CLOSE,
            Char.SQUARE_OPEN,
            Char.SQUARE_CLOSE,
            Char.QUOTE_DOUBLE,
            Char.QUOTE_SINGLE,
            Char.NEW_LINE,
            Char.UNDERSCORE,
            Char.VAR_,
            Char.VAR,
            None,
        ]:
            for c in Char:
                if c.value == value:
                    return c
            return None  


    class Operator(Enum):
        AND = "and"
        OR = "or"
        NOT = "not"

        @staticmethod
        def of(
            value: str,
        ) -> Union[
            Operator.AND,
            Operator.OR,
            Operator.NOT,
            None,
        ]:
            for c in Operator:
                if c.value == value:
                    return c
            return None  


    class IPredicate(EnumMeta):

        @classmethod
        def is_equality(self) -> bool:
            return False
        
        @classmethod
        def is_substring(self) -> bool:
            return False
        
        @classmethod
        def as_equality(self):
            raise # TODO

        @classmethod
        def as_substring(self):
            raise # TODO

    class Predicate:
        
        class Equality(Enum, metaclass=IPredicate):
            EQ = "="
            NEQ = "!="
            GT = ">"
            GTE = ">="
            LT = "<"
            LTE = "<="

            @staticmethod
            def of(
                value: str,
            ) -> Union[
                Equality.EQ,
                Equality.NEQ,
                Equality.GT,
                Equality.LT,
                Equality.LTE,
                None,
            ]:
                for c in Equality:
                    if c.value == value:
                        return c
                return None

            @classmethod
            def is_equality(self) -> bool:
                return True
            
            @classmethod
            def as_equality(self):
                return self

        class SubString(Enum, metaclass=Predicate):
            CONTAINS = "contains"
            LIKE = "like"

            @classmethod
            def is_substring(self):
                return True

            @classmethod         
            def as_substring(self):
                return self

            @staticmethod
            def of(
                value: str,
            ) -> Union[
                SubString.CONTAINS,
                SubString.LIKE,
                None,
            ]:
                for c in SubString:
                    if c.value == value:
                        return c
                return None


    class Schema(Enum):
        RULE = "rule"
        THEN = "then"
        WHEN = "when"

        @staticmethod
        def of(
            value: str,
        ) -> Union[
            Schema.RULE,
            Schema.THEN,
            Schema.WHEN,
            None,
        ]:
            for c in Schema:
                if c.value == value:
                    return c
            return None

    class Constraint(Enum):
        ABSTRACT "abstract"
        AS = "as"
        HAS = "has"
        IID = "iid"
        IS = "is"
        IS_KEY = "@key"
        ISA = "isa"
        ISAX = "isa!"
        OWNS = "owns"
        PLAYS = "plays"
        REGEX = "regex"
        RELATES = "relates"
        SUB = "sub"
        SUBX = "sub!"
        TYPE = "type"
        VALUE = ""
        VALUE_TYPE = "value"
    
        @staticmethod
        def of(
            value: str,
        ) -> Union[
            Constraint.ABSTRACT,
            Constraint.AS,
            Constraint.HAS,
            Constraint.IID
            Constraint.IS
            Constraint.ISA_KEY
            Constraint.ISAX
            Constraint.OWNS
            Constraint.PLAYS
            Constraint.REGEX
            Constraint.RELATES
            Constraint.SUB
            Constraint.SUBX
            Constraint.TYPE
            Constraint.VALUE
            Constraint.VALUE_TYPE
            None,
        ]:
            for c in Constraint:
                if c.value == value:
                    return c
            return None

    class Literal(Enum):
        TRUE = "true"
        FALSE = "false"

        @staticmethod
        def of(
            value: str,
        ) -> Union[
            Literal.TRUE,
            Literal.FALSE,
            None,
        ]:
            for c in Literal:
                if c.value == value:
                    return c
            return None
    
    class Aggregate:

        class Method(Enum):
            COUNT = "count"
            MAX = "max"
            MEAN = "mean"
            MEDIAN = "median"
            MIN = "min"
            STD ="std"
            SUM = "sum"
        
        @staticmethod
        def of(
            value: str,
        ) -> Union[
            Method.COUNT,
            Method.MAX,
            Method.MEAN,
            Method.MIN,
            Method.STD,
            Method.SUM,
            None,
        ]:
            for c in Method:
                if c.value == value:
                    return c
            return None

    class Compute:

        class Method(Enum):
            COUNT = "count"
            MIN = "min"
            MAX = "max"
            MEDIAN = "median"
            MEAN = "mean"
            STD = "std"
            SUM = "sum"
            PATH = "path"
            CENTRALITY ="centrality"
            CLUSTER = "cluster"
        
        @staticmethod
        def of(
            value: str,
        ) -> Union[
            Method.COUNT,
            Method.MIN,
            Method.MAX,
            Method.MEDIAN,
            Method.MEAN,
            Method.STD,
            Method.SUM,
            Method.PATH,
            Method.CENTRALITY,
            Method.CLUSTER,
            None,
        ]:
            for c in Method:
                if c.value == value:
                    return c
            return None

        class Condition(Enum):
            FROM = "from"
            TO = "to"
            OF = "of"
            IN = "in"
            USING = "using"
            WHERE = "where"
        
            @staticmethod
            def of(
                value: str,
            ) -> Union[
                Condition.FROM,
                Condition.TO,
                Condition.OF,
                Condition.IN,
                Condition.USING,
                Condition.WHERE,
                None,
            ]:
                for c in Condition:
                    if c.value == value:
                        return c
                return None
        
        class Param(Enum):
            MIN_K = "min-k"
            K = "k"
            CONTAINS = "contains"
            SIZE = "size"

            @staticmethod
            def of(
                value: str,
            ) -> Union[
                Param.MIN_K,
                Param.K,
                Param.CONTAINS,
                Param.SIZE,
                None,
            ]:
                for c in Param:
                    if c.value == value:
                        return c
                return None
