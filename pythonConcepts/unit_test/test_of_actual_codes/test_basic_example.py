import unittest

from pythonConcepts.unit_test.actual_code.basic_example import *

class TestBasicExample(unittest.TestCase):
    """
    Test class for basic test
    """

    def test_basic_example(self):
        val1 = 3
        val2 = 5
        expected = 8

        actual = basic_example(val1, val2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()