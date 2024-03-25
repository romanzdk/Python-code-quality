import unittest
from testy.app import add

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 4), 7)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_positive_and_negative_number(self):
        self.assertEqual(add(-5, 5), 0)

if __name__ == '__main__':
    unittest.main()
