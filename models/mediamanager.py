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
        with open(self.filename, "r") as fp:
            data = json.load(fp)

        self.types = []
        for items in PRESET_TYPE_DATA:
            for item in items:
                self.types.append(MediaType(item[0], item[1], item[2], item[3]))

        self.media = []
        
        for items in data:
            for types in self.types:
                self.media.append(Media(name=items['name'], med_type=types, field_1=['publisher'], field_2=['pages'], field_3=['genre']))

    """
    Add media instance to the manager's list of media
    """
    def add_media(self, name, type_name, field_1, field_2, field_3):
        self.media.append(Media(name, type_name, field_1, field_2, field_3))

    """
    Delete media instance matching name and type from the manager's list of media
    """
    def delete_media(self, name, type_name):
        for entry in self.media:
            if entry.name == name and entry.type.name == type_name:
                self.types.remove(entry)


    """
    Get a list of media entries that are a given type
    Return None if there are no results
    """

    def list_by_type(self, type):
        media_list = []
        for items in self.media:
            if items.types.name == type:
                media_list.append(items)
        
        return media_list

    """
    Return JSON compatible version of the list of media
    """

    def save(self):
        new_items = []
        for items in self.media:
            new_items.append(Media.to_dict(items))

        with open(self.filename, "w") as fp:
            data = json.dump(new_items, fp)
        
        return data
