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

    def __init__(self, data = []):
        self.types = []
        self.media = []

        for preset in PRESET_TYPE_DATA:
            self.types.append(MediaType(*preset))

        if len(data) == 0:
            return

        for data in data:
            m_type = self.search_for_type(data["type"])
            if m_type is None:
                self.add_type(data)
                m_type = self.search_for_type(data["type"])
            
            data_keys = [*data]
            self.media.append(Media(data["name"], m_type, data[data_keys[3]], data[data_keys[4]], data[data_keys[5]], data["_id"]))

    """
    Set local keys of media entries
    """   
    def set_local_keys(self):
        for entry in self.media:
            entry.local_key = self.media.index(entry) + 1


    """
    Return a MediaType instance with the specified name, None if not found
    """
    def search_for_type(self, name):
        for t in self.types:
            if t.name == name:
                return t
        return None

    """
    Add a MediaType to the list of MediaTypes, on top of the preset types

    Note: this will only execute when additional types need to be made when reading JSON data
    """
    def add_type(self, data):
        keys = [*data]
        new_type = MediaType(data["type"], keys[3], keys[4], keys[5])
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
    Delete media instance with matching key from the manager's list of media

    Returns True if something was deleted
    Returns False if unable to delete
    """

    def delete_media(self, key):
        to_delete = None
        for entry in self.media:
            if entry.local_key == key:
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
    Find media entry with specified key
    """
    
    def view_media(self, key):
        for media in self.media:
            if media.local_key == key:
                return media
        return None
