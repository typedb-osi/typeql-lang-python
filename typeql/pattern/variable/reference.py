from typeql.types.reference import ReferableT, ReferenceT
import re

class Referable(ReferenceT):
    def __init__(self, type: ReferenceT.Type, is_visible: bool):
        super().__init__(type, is_visible)

    def as_referable(self):
        return self



class Reference(ReferenceT):


    class Name(Referable):

        def __init__(self, name: str):
            super().__init__(self.Type.NAME, True)

            self._regex = re.compile('[a-zA-Z0-9][a-zA-Z0-9_-]*')

            #if self._regex.match():
                raise TypeQLException.of(INVALID_VARIABLE_NAME)
            
            self._name = name
            self._hash

        @property
        def name(self):
            return self._name

        @property
        def as_name(self):
            return self
        #def __hash__
        #def __eq__


    class Label(Referable):

        def __init__(self, label: str):
            super().__init__(self.Type.LABEL, False)
            self._label = label
            self._hash

        
        @property
        def label(self) -> str:
            return self._label

        def name(self) -> str:
            return TypeQLToken.Char.UNDERSCORE + label
        
        def as_label(self):
            return self

        #def __hash__
        #def __eq__



    class Anonymous(Referable):
        def __init__(self, is_visible: bool):
            super().__init__(self.Type.ANONYMOUS, is_visible)
            self._hash


    def __init__(self, type: ReferenceT.Type, is_visible: bool):
        self._type = type
        self._is_visible = is_visible

    def name(self, name: str) -> Reference.Name:
        return Name(name)

    def label(self, label: str) -> Reference.Label:
        return Label(label)

    def anonymous(self, is_visible: bool) -> Reference.Anonymous:
        return Reference.Anonymous(is_visible)


    def type(self) -> Reference.Type:
        return self._type


    def name(self):
        pass
    
    def syntax(self) -> str:
        return TypeQLToken.Char.$ + name()

    @property
    def is_visible(self) -> bool:
        return self._is_visible
    
    def is_anonymous(self) -> bool:
        return type == self.Type.ANONYMOUS 

    def is_label(self) -> bool:
        return type == self.Type.LABEL 

    def is_name(self) -> bool:
        return type == self.Type.NAME 


    def is_referable(self) -> bool:
        return !is_anonymous()

    def as_referable(self) -> Referable:
         return  TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, Referable.__class__.__name__
        )
    
    def as_label(self) -> Reference.Label:
        raise  TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, Label.__class__.__name__
        )
    
    def as_name(self) -> Reference.Name:
        raise  TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, Referable.__class__.__name__
        )
    
    def as_name(self) -> Reference.Anonymous:
        raise  TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, Anonymous.__class__.__name__
        )

    def __str__(self):
        return syntax()