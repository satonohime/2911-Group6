from media import Media
import pytest

@pytest.fixture
def media():
    media = Media('book1', 'book', 'publisher', 'length', 'genre')
    return media

@pytest.fixture
def media2():
    media2 = Media('song1', 'music', 'artist', 'album', 'year')
    return media2

def test_Media(media):
    assert type(media) is Media
    assert media.name == 'book1'
    assert media.type == 'book'
    assert media.f1 == 'publisher'
    assert media.f2 == 'length'
    assert media.f3 == 'genre'

def test_Media_invalid():
    with pytest.raises(TypeError):
        invalid_Media = Media(123, '123', '123', '123', '123')
    with pytest.raises(TypeError):
        invalid_Media = Media('123', 123, '123', '123', '123')
    with pytest.raises(TypeError):
        invalid_Media = Media('123', '123', 123, '123', '123')
    with pytest.raises(TypeError):
        invalid_Media = Media('123', '123', '123', 123, '123')
    with pytest.raises(TypeError):
        invalid_Media = Media('123', '123', '123', '123', 123)

def test_to_dict(media):
    result = media.to_dict()
    assert result['name'] == media.name
    assert result['type'] == media.type
    assert result['f1'] == media.f1
    assert result['f2'] == media.f2
    assert result['f3'] == media.f3