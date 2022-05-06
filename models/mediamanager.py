from models.media import Media
from models.mediatype import MediaType
import json

PRESET_TYPE_DATA = [
    ["music", "artist", "album", "genre"],
    ["book", "author", "publisher", "genre"],
    ["movie", "genre", "year", "length"],
    ["game", "main_platform", "publisher", "genre"],
]


class MediaManager:
    """
    Represents a collection of Media

    Attributes:
        filename: name of the file to read
        types: a list of MediaTypes
        media: a list of all the Media instances
    """

    def __init__(self, filename: str = "data/media.json"):
        self.filename = filename
        self.types = []
        self.media = []

        for preset in PRESET_TYPE_DATA:
            self.types.append(MediaType(*preset))

        with open(self.filename) as fp:
            json_data = json.load(fp)
            for data in json_data:
                m_type = self.search_for_type(data["type"])
                if m_type is None:
                    self.add_type(data)
                    m_type = self.search_for_type(data["type"])
                
                data_keys = [*data]
                self.media.append(Media(data["name"], m_type, data[data_keys[2]], data[data_keys[3]], data[data_keys[4]]))


    """
    Helper function
    Return a MediaType instance with the specified name, None if not found
    """
    def search_for_type(self, name):
        for t in self.types:
            if t.name == name:
                return t
        return None

    """
    Helper function
    Add a MediaType to the list of MediaTypes, on top of the preset types

    Note: this will only execute when additional types need to be made when reading JSON data
    """
    def add_type(self, data):
        keys = [*data]
        new_type = MediaType(data["type"], keys[2], keys[3], keys[4])
        self.types.append(new_type)

    """
    Add media instance to the manager's list of media
    """

    def add_media(self, name, type_name, field_1, field_2, field_3):
        m_type = self.search_for_type(type_name)
        if m_type is None:
            raise ValueError
        else:
            self.media.append(Media(name, m_type, field_1, field_2, field_3))

    """
    Delete media instance matching name and type from the manager's list of media

    Returns True if something was deleted
    Returns False if unable to delete
    """

    def delete_media(self, name, type_name):
        to_delete = None
        for entry in self.media:
            if entry.name == name and entry.type.name == type_name:
                to_delete = entry
                break
        if to_delete is not None:
            self.media.remove(to_delete)
            return True
        else:
            return False

    """
    Get a list of media entries that are a given type
    Return None if there are no results
    """

    def list_by_type(self, type):
        media_entries = []
        for entry in self.media:
            if entry.type.name == type:
                media_entries.append(entry)

        if len(media_entries) == 0:
            return None
        else:
            return media_entries


    """
    Write JSON compatible version of the list of media to a file
    """

    def save(self):
        with open(self.filename, "w") as fp:
            json.dump([entry.to_dict() for entry in self.media], fp)
        

    """
    Find media entry with specified name and type
    """
    def view_media(self, name, type):
        for media in self.media:
            if media.type.name == type and media.name == name:
                return media
        return None

        
