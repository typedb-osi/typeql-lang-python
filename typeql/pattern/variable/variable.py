from typeql.types.variable import VariableT
from typeql.common.exception.typeql_exception import TypeQLException, INVALID_CASTING


class Variable(VariableT):

    def __init__(self, reference: ReferenceT):
        self._reference = reference

    @property
    def constraints(self):
        pass

    def is_unbound(self) -> bool:
        return False
    
    def is_bound(self) -> bool:
        return False

    def is_concept(self) -> bool:
        return False

    def is_type(self) -> bool:
        return False

    def is_thing(self) -> bool:
        return False

    def as_unbound(self):
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, UnboundVariable.__class__.__name__
        )

    def as_bound(self):
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, BoundVariable.__class__.__name__
        )

    def variables(self):
        #TODO
        pass

    @property
    def type(self):
        return self._reference.type()

    @property
    def name(self):
        if self._reference.type() == NAME:
            return self._reference.as_name.name()
        else:
            return None

    @property
    def reference(self):
        return self._reference

    def is_named(self) -> bool:
        return self._reference.is_named()

    def is_labelled(self) -> bool:
        return self._reference.is_labelled()
    
    def is_anonymised(self) -> bool:
        return self._reference.is_anonymous()

    def is_visible(self) -> bool:
        return self._reference.is_visible()
