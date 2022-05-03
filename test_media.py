from media import Media
from mediatype import MediaType
import pytest

@pytest.fixture
def media():
    book_type = MediaType('book', 'publisher', 'length', 'genre')
    media = Media('book1', book_type, 'pub1', '10', 'Fantasy')
    return media

@pytest.fixture
def media2():
    music_type = MediaType('music', 'artist', 'album', 'year')
    media2 = Media('song1', music_type, 'artist1', 'album1', '2022')
    return media2

def test_Media(media):
    assert type(media) is Media
    assert media.name == 'book1'
    assert media.type.name == 'book'
    assert media.type.field_1 == 'publisher'
    assert media.type.field_2 == 'length'
    assert media.type.field_3 == 'genre'
    assert media.field_1 == 'pub1'
    assert media.field_2 == '10'
    assert media.field_3 == 'Fantasy'

def test_Media_invalid():
    test_type = MediaType('test', 'test', 'test', 'test')
    with pytest.raises(TypeError):
        invalid_Media = Media(123, test_type, '123', '123', '123')
    with pytest.raises(TypeError):
        invalid_Media = Media('123', 123, '123', '123', '123')
    with pytest.raises(TypeError):
        invalid_Media = Media('123', test_type, 123, '123', '123')
    with pytest.raises(TypeError):
        invalid_Media = Media('123', test_type, '123', 123, '123')
    with pytest.raises(TypeError):
        invalid_Media = Media('123', test_type, '123', '123', 123)

def test_to_dict(media):
    result = media.to_dict()
    assert result['name'] == media.name
    assert result['type'] == media.type.name
    assert result['f1'] == media.field_1
    assert result['f2'] == media.field_2
    assert result['f3'] == media.field_3