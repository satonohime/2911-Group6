from models.media import Media
from models.mediatype import MediaType
import json

PRESET_TYPE_DATA = [
    ['music', 'artist', 'album', 'genre'],
    ['book', 'author', 'publisher', 'genre'],
    ['game', 'main_platform', 'publisher' ,'genre']
]

class MediaManager:
    """
    Represents a collection of Media

    Attributes:
        filename: name of the file to read
        types: a list of MediaTypes
    """

    def __init__(self, filename: str = "data/media.json"):
        self.filename = filename
        self.types = []
        self.media = []

    """
    Add media instance to the manager's list of media
    """
    def add_media(self, name, type_name, field_1, field_2, field_3):
        pass

    """
    Delete media instance matching name and type from the manager's list of media
    """
    def delete_media(self, name, type_name):
        pass


    """
    Get a list of media entries that are a given type
    Return None if there are no results
    """

    def list_by_type(self, type):
        pass

    """
    Return JSON compatible version of the list of media
    """

    def save(self):
        pass
