import unittest
from main import get_max_sub_array

class TestMaxSubarrayMethods(unittest.TestCase):

    def test_only_positive(self):
        self.assertEqual(get_max_sub_array([2, 1, 3, 4, 1, 2, 1, 5, 4]), ([2, 1, 3, 4, 1, 2, 1, 5, 4], 23))

    def test_only_negative(self):
        self.assertEqual(get_max_sub_array([-2, -1, -3, -4, -1, -2, -1, -5, -4]), ([-1], -1))

    def test_mixed(self):
        self.assertEqual(get_max_sub_array([-2, -1, 3, 4, -1, -2, -1, 5, -4, -1, -2, -1, 5, 4]), ([5, 4], 9))

    def test_empty(self):
        with self.assertRaises(ValueError):
            get_max_sub_array([])

    def test_char_in_array(self):
        with self.assertRaises(TypeError):
            get_max_sub_array([0, 'a'])
            

if __name__ == '__main__':
    unittest.main()