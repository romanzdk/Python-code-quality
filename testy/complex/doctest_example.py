class ListManager:
    """
    A simple class to manage a list.

    >>> manager = ListManager()  # Setup
    >>> manager.add_item('item1')  # Test add_item
    >>> 'item1' in manager.get_items()
    True
    >>> manager.remove_item('item1')  # Test remove_item
    True
    >>> 'item1' in manager.get_items()  # Verify item is removed
    False
    >>> manager.add_item('item2')  # Additional setup for remove test
    >>> manager.remove_item('nonexistent')  # Test remove non-existent item
    False
    >>> del manager  # Teardown (if necessary)
    """
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Adds an item to the list."""
        self.items.append(item)

    def remove_item(self, item):
        """Removes an item from the list if it exists."""
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def get_items(self):
        """Returns a copy of the list of items."""
        return self.items.copy()