from __future__ import annotations

from enum import Enum, EnumMeta
from typing import Optional, Union


class TypeQLArg:
    class QueryType(Enum):
        READ = 0
        WRITE = 1

        @classmethod
        def is_write(self) -> bool:
            if self.WRITE:
                return True
            else:
                return False

        @classmethod
        def is_read(self) -> bool:
            if self.READ:
                return True
            else:
                return False

        @classmethod
        def of(cls, value: str) -> Union[QueryType.READ, QueryType.WRITE, None]:
            for c in cls:
                if c.value == value:
                    return c
            return None

    class ValueType(Enum):
        BOOLEAN = "boolean"
        DATETIME = "datetime"
        DOUBLE = "double"
        LONG = "long"
        STRING = "string"

    class Order(Enum):
        ASC = "asc"
        DESC = "desc"

        @classmethod
        def of(cls, value: str) -> Union[Order.ASC, Order.DESC, None]:
            for c in cls:
                if c.value == value:
                    return c
            return None

    class Algorithm(Enum):
        DEGREE = "degree"
        K_CORE = "k_core"
        CONNECTED_COMPONENT = "connected-component"

        @classmethod
        def of(
            cls, value: str,
        ) -> Union[
            Algorithm.DEGREE, Algorithm.K_CORE, Algorithm.CONNECTED_COMPONENT, None
        ]:
            for c in cls:
                if c.value == value:
                    return c
            return None
