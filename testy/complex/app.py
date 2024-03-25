class ListManager:
    """A simple class to manage a list."""
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