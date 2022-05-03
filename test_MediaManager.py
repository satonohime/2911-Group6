from models.mediamanager import MediaManager
import pytest
from unittest.mock import mock_open, patch

JSON_FILE = """[
    {"name": "test1", "type": "test_type1", "field_1": "test_f1", "field_2": "test_f2", "field_3": "test_f3"}, 
    {"name": "test2", "type": "test_type1", "field_1": "test_f1", "field_2": "test_f2", "field_3": "test_f3"},
    {"name": "test3", "type": "test_type1", "field_1": "test_f1", "field_2": "test_f2", "field_3": "test_f3"},
    {"name": "test4", "type": "test_type1", "field_1": "test_f1", "field_2": "test_f2", "field_3": "test_f3"}
]"""


@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=JSON_FILE)
def med_manager(mock_file):
    med_manager = MediaManager()
    mock_file.assert_called_once()
    assert "data/media.json" in mock_file.call_args[0]
    assert len(med_manager.types) == 1
    assert med_manager.types[0].name == "test_type1"
    return med_manager

def test_list_by_type(med_manager):
    assert len(med_manager.list_by_type('test_type1')) == 4
    assert len(med_manager.list_by_type('test_type2')) is None

def test_add_type(med_manager):
    med_manager.add_type('test_type2', 'new_field1', 'new_field2', 'new_field3')
    assert ['test_type2', 'new_field1', 'new_field2', 'new_field3'] in med_manager.types

def test_add_type_already_exists(med_manager):
    with pytest.raises(RuntimeError):
        med_manager.add_type('test_type1', 'data1', 'data2', 'data3')

def test_delete_type(med_manager):
    med_manager.add_type('test_type2', 'new_field1', 'new_field2', 'new_field3')
    assert len(med_manager.types) == 2
    med_manager.delete_type('test_type2')
    assert len(med_manager.types) == 1
    assert med_manager.types[0].name == "test_type1"

def test_delete_type_invalid(med_manager):
    with pytest.raises(RuntimeError):
        med_manager.delete_type('test_type1')

@patch("builtins.open", new_callable=mock_open)
def test_save(mock_file, med_manager):
    med_manager.save()
    mock_file.assert_called_once_with("data/residents.json", "w")