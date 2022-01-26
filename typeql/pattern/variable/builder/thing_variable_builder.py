from multipledispatch import dispatch

class ThingVariableBuilder(ThingVariableBuilderT):

    @dispatch(TypeQLToken.Type)
    def isa(self, type):
    
    @dispatch(str)
    def isa(self, type):
    
    @dispatch(UnboundVariable)
    def isa(self, type):
    
    @dispatch(TypeQLToken.Type)
    def isaX(self, type):
    
    @dispatch(str)
    def isaX(self, type):
    
    @dispatch(UnboundVariable)
    def isaX(self, var):
    
