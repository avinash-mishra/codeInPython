import unittest
from pythonConcepts.unit_test.actual_code.multiple_methods import MultipleMethod


class TestMultipleMethod(unittest.TestCase):
    """
    Test class for MultipleMethods
    """

    # def __init__(self):
    #     a = 2
    #     b = 3

    def setUp(self):
        print("Setup")
        self.val1 = 3
        self.val2 = 5

    def test_sum(self):
        expected = 8
        actual = MultipleMethod.sum_method(self.val1, self.val2)
        self.assertEqual(expected, actual)

    def test_subtract(self):
        expected = -2
        actual = MultipleMethod.subtract_method(self.val1, self.val2)
        self.assertEqual(expected, actual)

    def tearDown(self):
        print("TearDown")
        del self.val1, self.val2


if __name__ == '__main__':
    unittest.main()
