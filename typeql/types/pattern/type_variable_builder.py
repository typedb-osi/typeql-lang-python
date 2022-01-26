import abc

class TypeVariableBuilderT(abc.ABC):

    @abc.abstractmethod
    def type(self, scope, type, label):
        ...

    @abc.abstractmethod
    def is_abstract(self):
        ...

    @abc.abstractmethod
    def sub(self, type, type_scope, type_label, type_var):
        ...

    @abc.abstractmethod
    def subX(self, type, type_scope, type_label, type_var):
        ...

    @abc.abstractmethod
    def owns(self, attribute_type, attribute_type_var, overridden_attribute_type, is_key):
        ...

    @abc.abstractmethod
    def plays(
        slef,
        relation_type,
        role_type,
        role_typevar,
        overridden_role_type,
        overridden_role_type_var,
    ):
        ...

    @abc.abstractmethod
    def relates(
        self, 
        role_type,
        role_type_var, 
        overridden_role_type, 
        overridden_role_type_var
    ):
        ...

    @abc.abstractmethod
    def value(self, value_type):
        ...
    
    @abc.abstractmethod
    def regex(self, regex):
        ...

    @abc.abstractmethod
    def constrain(constraint):
        ...
