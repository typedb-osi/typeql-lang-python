from enum import enum


class Type(Enum):
    NAME
    LABEL
    ANONYMOUS

class Reference():

    def __init__(self, t, is_visible):
        self._type = t
        self._is_visible = is_visible

    def name(self, name):
    
    def label(self, label):
    
    def anonymous(self, is_visible):
        