from multipledispatch import dispatch

class ConceptVariableBuilder(ConceptVariableBuilderT):

    @dispatch(str)
    def is(self, var):
    
    @dispatch(UnboundVariable)
    def is(self, var):
    