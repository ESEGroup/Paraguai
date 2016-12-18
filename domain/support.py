class ValueObject():
    def __eq__(self, other):
        return (
            self.__dict__ == other.__dict__
            and
            self.__class__ == other.__class__
            )

    def __ne__(self, other):
        return not (self == other)

class ID(ValueObject):
    def __init__(self, id):
        self.id = id

    def __int__(self):
        return self.id
