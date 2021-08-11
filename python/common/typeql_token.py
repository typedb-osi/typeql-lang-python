from __future__ import annotations

from enum import Enum, EnumMeta
from typing import Optional, Union


class IPredicate(EnumMeta):
    @classmethod
    def is_equality(self) -> bool:
        return False

    @classmethod
    def is_substring(self) -> bool:
        return False

    @classmethod
    def as_equality(self):
        pass
        # TODO raise

    @classmethod
    def as_substring(self):
        pass
        # TODO raise


class TypeQLToken:
    class Type(Enum):
        THING = "thing"
        ENTITY = "entity"
        ATTRIBUTE = "attribute"
        RELATION = "relation"
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

        @classmethod
        def of(
            cls, value: str,
        ) -> Union[
            Command.COMPUTE,
            Command.DEFINE,
            Command.UNDEFINE,
            Command.INSERT,
            Command.MATCH,
            Command.AGGREGATE,
            Command.GROUP,
            None,
        ]:
            for c in cls:
                if c.value == value:
                    return c
            return None
        
        def __str__(self)->str:
            return str(self.value)


    class Filter(Enum):
        GET = "get"
        SORT = "sort"
        OFFSET = "offset"
        LIMIT = "limit"

        @classmethod
        def of(
            cls, value: str,
        ) -> Union[Filter.GET, Filter.SORT, Filter.OFFSET, Filter.LIMIT, None]:
            for c in cls:
                if c.value == value:
                    return c
            return None
        
        def __str__(self)->str:
            return str(self.value)

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
        QUOTE_DOUBLE = '"'
        QUOTE_SINGLE = "'"
        NEW_LINE = "\n"
        UNDERSCORE = "_"
        VAR_ = "$_"
        VAR = "$"

        @classmethod
        def of(
            cls, value: str,
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
            for c in cls:
                if c.value == value:
                    return c
            return None
        
        def __str__(self)->str:
            return str(self.value)


    class Operator(Enum):
        AND = "and"
        OR = "or"
        NOT = "not"

        @classmethod
        def of(cls, value: str) -> Union[Operator.AND, Operator.OR, Operator.NOT, None]:
            for c in cls:
                if c.value == value:
                    return c
            return None
        
        def __str__(self)->str:
            return str(self.value)

    class Predicate:
        class Equality(Enum, metaclass=IPredicate):
            EQ = "="
            NEQ = "!="
            GT = ">"
            GTE = ">="
            LT = "<"
            LTE = "<="

            @classmethod
            def of(
                cls, value: str,
            ) -> Union[
                Equality.EQ, Equality.NEQ, Equality.GT, Equality.LT, Equality.LTE, None
            ]:
                for c in cls:
                    if c.value == value:
                        return c
                return None

            @classmethod
            def is_equality(self) -> bool:
                return True

            @classmethod
            def as_equality(self):
                return self

            def __str__(self)->str:
                return str(self.value)
        class SubString(Enum, metaclass=IPredicate):
            CONTAINS = "contains"
            LIKE = "like"

            @classmethod
            def is_substring(self):
                return True

            @classmethod
            def as_substring(self):
                return self

            @classmethod
            def of(cls, value: str) -> Union[SubString.CONTAINS, SubString.LIKE, None]:
                for c in cls:
                    if c.value == value:
                        return c
                return None
            
            def __str__(self)->str:
                return str(self.value)

    class Schema(Enum):
        RULE = "rule"
        THEN = "then"
        WHEN = "when"

        @classmethod
        def of(cls, value: str) -> Union[Schema.RULE, Schema.THEN, Schema.WHEN, None]:
            for c in cls:
                if c.value == value:
                    return c
            return None

        def __str__(self)->str:
            return str(self.value)

    class Constraint(Enum):
        ABSTRACT = "abstract"
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

        @classmethod
        def of(
            cls, value: str,
        ) -> Union[
            Constraint.ABSTRACT,
            Constraint.AS,
            Constraint.HAS,
            Constraint.IID,
            Constraint.IS,
            Constraint.ISA_KEY,
            Constraint.ISAX,
            Constraint.OWNS,
            Constraint.PLAYS,
            Constraint.REGEX,
            Constraint.RELATES,
            Constraint.SUB,
            Constraint.SUBX,
            Constraint.TYPE,
            Constraint.VALUE,
            Constraint.VALUE_TYPE,
            None,
        ]:
            for c in cls:
                if c.value == value:
                    return c
            return None

        def __str__(self)->str:
            return str(self.value)

    class Literal(Enum):
        TRUE = "true"
        FALSE = "false"

        @classmethod
        def of(cls, value: str) -> Union[Literal.TRUE, Literal.FALSE, None]:
            for c in cls:
                if c.value == value:
                    return c
            return None
        
        def __str__(self)->str:
            return str(self.value)
    class Aggregate:
        class Method(Enum):
            COUNT = "count"
            MAX = "max"
            MEAN = "mean"
            MEDIAN = "median"
            MIN = "min"
            STD = "std"
            SUM = "sum"

            @classmethod
            def of(
                cls, value: str,
            ) -> Union[
                Method.COUNT,
                Method.MAX,
                Method.MEAN,
                Method.MIN,
                Method.STD,
                Method.SUM,
                None,
            ]:
                for c in cls:
                    if c.value == value:
                        return c
                return None

            def __str__(self)->str:
                return str(self.value)

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
            CENTRALITY = "centrality"
            CLUSTER = "cluster"

            @classmethod
            def of(
                cls, value: str,
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
                for c in cls:
                    if c.value == value:
                        return c
                return None

            def __str__(self)->str:
                return str(self.value)

        class Condition(Enum):
            FROM = "from"
            TO = "to"
            OF = "of"
            IN = "in"
            USING = "using"
            WHERE = "where"

            @classmethod
            def of(
                cls, value: str,
            ) -> Union[
                Condition.FROM,
                Condition.TO,
                Condition.OF,
                Condition.IN,
                Condition.USING,
                Condition.WHERE,
                None,
            ]:
                for c in classmethod:
                    if c.value == value:
                        return c
                return None

            def __str__(self)->str:
                return str(self.value)
        class Param(Enum):
            MIN_K = "min-k"
            K = "k"
            CONTAINS = "contains"
            SIZE = "size"

            @classmethod
            def of(
                cls, value: str,
            ) -> Union[Param.MIN_K, Param.K, Param.CONTAINS, Param.SIZE, None]:
                for c in Param:
                    if c.value == value:
                        return c
                return None

            def __str__(self)->str:
                return str(self.value)