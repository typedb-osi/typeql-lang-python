

class Computable(ABC):

    @abstracmethod
    def method(self):
        pass

    def conditions_required():
        pass
    
    def get_exception():
        pass

class Argument(ABC):
    def _type():
        pass
    
    def value():
        pass

class Arguments(ABC):
    def _min_K():
        pass
    
    def _k():
        pass

    def _size():
        pass
    
    def _contains():
        pass


class Targetable(Computable):
    
    def of(self, type, types):
        pass
    

class Scopeable(Computable):

    def includes_attributes():
        pass
    
    def in(self, type, types):
        pass
    
    def attributes(self, include):
        pass


class Configurable(Computable):

    def using():
        pass
    
    def where():
        pass
    
    def algorithms_accepted():
        pass
    
    def argumentes_default():
        pass