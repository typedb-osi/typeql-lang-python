

from typeql_python.common.exception.typeql_exception import TypeQLException, INVALID_CASTING
from typeql_python.types.definable import DefinableT

class Definable(DefinableT):

    def is_rule(self):
        return False

    def is_type_variable(self):
        return False

    def as_rule(self):
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, Rule.__class__.__name__
        )

    def as_type_variable(self):
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, TypeVariable.__class__.__name__
        )