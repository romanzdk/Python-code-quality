import unittest
from testy.complex.app import ListManager

class TestListManager(unittest.TestCase):

    def setUp(self):
        """Setup method to create a ListManager instance before each test."""
        self.list_manager = ListManager()

    def tearDown(self):
        """Teardown method to delete the ListManager instance after each test."""
        del self.list_manager

    def test_add_item(self):
        """Test adding items."""
        self.list_manager.add_item('item1')
        self.assertIn('item1', self.list_manager.get_items())

    def test_remove_item(self):
        """Test removing items."""
        self.list_manager.add_item('item1')
        self.assertTrue(self.list_manager.remove_item('item1'))
        self.assertNotIn('item1', self.list_manager.get_items())

    def test_remove_nonexistent_item(self):
        """Test removing an item that doesn't exist."""
        self.assertFalse(self.list_manager.remove_item('nonexistent'))

if __name__ == '__main__':
    unittest.main()
