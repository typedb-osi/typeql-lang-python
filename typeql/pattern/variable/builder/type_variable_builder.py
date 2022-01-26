from multipledispatch import dispatch

class TypeVariableBuilder(TypeVariableBuilderT):

    @dispatch(TypeQLToken.Type)
    def type(self, type):

    @dispatch(str)
    def type(self, label):
    
    @dispatch(str, str)
    def type(self, scope, label):
    
    @dispatch(TypeQLToken.Type)
    def sub(self, type):
    
    @dispatch(str)
    def sub(self, type_label):
    
    @dispatch(str, str)
    def sub(self, type_scope, type_label):
    
    @dispatch(UnboundVariable)
    def sub(self, type_var):
    
    @dispatch(TypeQLToken.Type)
    def subX(self, type):
    
    @dispatch(str)
    def subX(self, type_label):
    
    @dispatch(str, str)
    def subX(self, type_scope, type_label):
    
    @dispatch(UnboundVariable)
    def subX(self, type_var):

    @dispatch(str)
    def owns(self, attribute_type):
    
    @dispatch(str, bool)
    def owns(self, attribute_type, is_key):
    
    @dispatch(UnboundVariable)
    def owns(self, attribute_type_var):
    
    @dispatch(UnboundVariable, bool)
    def owns(self, attribute_type_var, is_key):
    
    @dispatch(str, str)
    def owns(self, attribute_type, overridden_attribute_type):
    
    @dispatch(str, UnboundVariable)
    def owns(self, attribute_type, overridden_attribute_type):
    
    @dispatch(str, UnboundVariable, bool)
    def owns(self, attribute_type, overridden_attribute_type, is_key):
   
    @dispatch(UnboundVariable, str)
    def owns(self, attribute_type_var, overridden_attribute_type):
    
    @dispatch(UnboundVariable, str, bool)
    def owns(self, attribute_type_var, overridden_attribute_type, is_key):
    
    @dispatch(UnboundVariable, UnboundVariable)
    def owns(self, attribute_type_var, overridden_attribute_type):
    
    @dispatch(UnboundVariable, UnboundVariable, bool)
    def owns(self, attribute_type_var, overridden_attribute_type, is_key):

    @dispatch(str, str)
    def plays(self, relation_type, role_type):
    
    @dispatch(UnboundVariable)
    def plays(self, role_type_var):

    @dispatch(str, str, str)
    def plays(self, relation_type, role_type, overridden_role_type):
    
    @dispatch(UnboundVariable, str)
    def plays(self, role_type_var, overridden_role_type):
    
    @dispatch(UnboundVariable, UnboundVariable)
    def plays(self, role_type_var, overridden_role_type_var):

    @dispatch(str)
    def relates(self, role_type):
    
    @dispatch(UnboundVariable)
    def relates(self, role_type_var):
    
    @dispatch(str, str)
    def relates(self, role_type, overridden_role_type):

    @dispatch(str, UnboundVariable)
    def relates(self, role_type, overridden_role_type_var):

    @dispatch(UnboundVariable, str)
    def relates(self, role_type_var, overridden_role_type)

    @dispatch(UnboundVariable, UnboundVariable)
    def relates(self, role_type_var, overridden_role_type_var)

    def value(self, value_type: TypeQLArg.ValueType):

    def regex(regex: str):
    
    def constrain(self, constraint) -> TypeVariable: