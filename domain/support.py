class ValueObject():
    def __eq__(self, other):
        try:
            return (
                self.__dict__ == other.__dict__
                and
                self.__class__ == other.__class__
                )
        except AttributeError:
            return False

    def __ne__(self, other):
        return not (self == other)
