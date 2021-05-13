from abc import ABC, abstractmethod


class ITypeVariableBuilder(ABC):
    @abstractmethod
    def kind(self, scope, type, label):
        pass

    @abstractmethod
    def is_abstract(self):
        pass

    @abstractmethod
    def sub(self, type, typeScope, typeLabel, typeVar):
        pass

    @abstractmethod
    def subX(self, type, typeScope, typeLabel, typeVar):
        pass

    @abstractmethod
    def owns(self, attributeType, attributeTypeVar, overriddenAttributeType, isKey):
        pass

    @abstractmethod
    def plays(
        slef,
        relationType,
        roleType,
        roleTypevar,
        overriddenRoleType,
        overriddenRoleTypeVar,
    ):
        pass

    @abstractmethod
    def relates(self, roleType, roleTypeVar, overriddenRoleType, overriddenRoleTypeVar):
        pass

    @abstractmethod
    def value(self, ValueType):
        pass

    @abstractmethod
    def regex(self, regex):
        pass

    @abstractmethod
    def constrain(constraint):
        pass
