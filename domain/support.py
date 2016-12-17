class ValueObject():
    def __eq__(self, other):
        self.__dict__ == other.__dict__ && self.__class__ == other.__class__

class ID(ValueObject):
    def __init__(self, id):
        self.id = id
