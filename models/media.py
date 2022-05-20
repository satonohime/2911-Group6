from .mediatype import MediaType

class Media:
    """
    Represents an instance of a piece of media

    Attributes:
        name: name
        type: the MediaType of the media
        field_1 to field_3: The values of the three fields of the MediaType
    """

    def __init__(self, name, med_type: MediaType, field_1, field_2, field_3, _id = None):
        for item in [name, field_1, field_2, field_3]:
            if type(item) is not str:
                raise TypeError
        if type(med_type) is not MediaType:
            raise TypeError
        self.name = name
        self.type = med_type
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3
        self.local_key = None
        self._id = _id

    """
    Convert media entry to JSON compatible dict data
    """

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type.name,
            self.type.field_1: self.field_1,
            self.type.field_2: self.field_2,
            self.type.field_3: self.field_3,
            "local_key": self.local_key
        }

