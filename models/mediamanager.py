from media import Media
import json

class MediaManager:
    """
    Represents a collection of Media

    Attributes:
        filename: name of the file to read
        types: a list of types (see functions below)
    """
    def __init__(self, filename: str = "data/media.json"):
        self.filename = filename
        self.types = []
        self.media = []

    """
    Create a media type with the format [name, type, field_1, field_2, field_3]
    You are not allowed to create a type if it already exists, even with different fields
    """
    def create_type(self, type, f1, f2, f3):
        pass

    """
    Delete a type from the MediaManager
    You are not allowed to delete a type if an entry in the collection has that type
    """
    def delete_type(self, type):
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



