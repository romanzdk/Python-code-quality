from testy.complex.app import ListManager

import pytest

@pytest.fixture
def list_manager():
    """Fixture to create a ListManager instance before each test."""
    return ListManager()

def test_add_item(list_manager):
    """Test adding items."""
    list_manager.add_item('item1')
    assert 'item1' in list_manager.get_items()

def test_remove_item(list_manager):
    """Test removing items."""
    list_manager.add_item('item1')
    assert list_manager.remove_item('item1')
    assert 'item1' not in list_manager.get_items()

def test_remove_nonexistent_item(list_manager):
    """Test removing an item that doesn't exist."""
    assert not list_manager.remove_item('nonexistent')
