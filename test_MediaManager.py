from models.mediamanager import MediaManager
import pytest
from unittest.mock import mock_open, patch

JSON_FILE = """[
    {"name": "test1", "type": "test_type1", "field_1": "test_f1", "field_2": "test_f2", "field_3": "test_f3"}, 
    {"name": "test2", "type": "test_type1", "field_1": "test_f1", "field_2": "test_f2", "field_3": "test_f3"},
    {"name": "test3", "type": "test_type2", "f1": "dog", "f2": "cat", "f3": "bird"},
    {"name": "test4", "type": "test_type2", "f1": "dog", "f2": "cat", "f3": "bird"}
]"""


@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=JSON_FILE)
def med_manager(mock_file):
    med_manager = MediaManager()
    return med_manager


@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_med_manager_open(mock_file):
    med_manager = MediaManager()
    mock_file.assert_called_once()
    assert "data/media.json" in mock_file.call_args[0]


def test_med_manager_init():
    assert len(med_manager.types) == 2
    assert med_manager.types[0].name == "test_type1"

def test_add_media():
    med_manager.add_media('test7', 'test_type1', 'chicken', 'chicken', 'chicken')
    assert len(med_manager.list_by_type("test_type1")) == 3
    assert len(med_manager.media) == 5
    assert med_manager.media[4].type.name == 'test_type1'

def test_delete_media():
    med_manager.delete_media('test1', 'test_type1')
    assert len(med_manager.list_by_type("test_type1")) == 1
    assert len(med_manager.media) == 3


def test_list_by_type(med_manager):
    assert len(med_manager.list_by_type("test_type1")) == 2
    assert len(med_manager.list_by_type("test_type2")) == 2
    assert len(med_manager.list_by_type("test_type3")) is None


@patch("builtins.open", new_callable=mock_open)
def test_save(mock_file, med_manager):
    med_manager.save()
    mock_file.assert_called_once_with("data/media.json", "w")
