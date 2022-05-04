from models.mediatype import MediaType

class Media:
    """
    Represents an instance of a piece of media

    Attributes:
        name: name
        type: the type of the media
        field_1 to field_3: user defined fields that they want to track
    """
    def __init__(self, name, type: MediaType, f1, f2, f3):
        self.name = name
        self.type = type
        self.field_1 = f1
        self.field_2 = f2
        self.field_3 = f3


    """
    Convert media entry to JSON compatible dict data
    """
    def to_dict(self):
        data_dict = {
            'name': self.name,
            'type': self.type,
            'field_1': self.field_1,
            'field_2': self.field_2,
            'field_3': self.field_3
        }

        return data_dict