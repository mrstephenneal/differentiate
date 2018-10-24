# Retrieve unique values from two nested lists.
import unittest
from differentiate import diff
from looptools import Timer


class TestDiffInts(unittest.TestCase):
    @Timer.decorator
    def test_diff_int_nested(self):
        x = [[0, 1, 2, 3, 4],
             [5, 6, 7, 8, 9],
             [10, 11, 12, 13, 14]]
        y = [[5, 6, 7, 8, 9],
             [10, 11, 12, 13, 14],
             [15, 16, 17, 18, 19]]

        uniques = diff(x, y)
        self.assertEqual(len(uniques), 2)

    @Timer.decorator
    def test_diff_int_flat(self):
        x = [0, 1, 2, 3, 4]
        y = [3, 4, 5, 6, 7]

        uniques = diff(x, y)
        self.assertEqual(len(uniques), 6)

    @Timer.decorator
    def test_diff_int_duplicates(self):
        x = [0, 1, 2, 3, 4]
        y = [3, 4, 5, 6, 7]

        uniques = diff(x, y, duplicates=True)
        self.assertEqual(len(uniques), 2)


if __name__ == '__main__':
    unittest.main()
