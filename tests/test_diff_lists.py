import unittest
from differentiate import diff
from looptools import Timer


class TestDiffLists(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.existing = [['d001', 'Marketing'], ['d002', 'Finance'], ['d003', 'Human Resources'], ['d004', 'Production'],
                        ['d005', 'Development'], ['d006', 'Quality Management'], ['d007', 'Sales'],
                        ['d008', 'Research'], ['d009', 'Customer Service']]
        cls.new = [['d009', 'Customer Service'], ['d002', 'Finance'], ['d010', 'Information Technology'],
                   ['d011', 'Software Development']]

    @Timer.decorator
    def test_diff_list(self):
        diffs = diff(self.new, self.existing)
        self.assertEqual(len(diffs), 9)

    @Timer.decorator
    def test_diff_list_x_only(self):
        diffs = diff(self.new, self.existing, x_only=True)
        self.assertEqual(len(diffs), 2)

    @Timer.decorator
    def test_diff_list_y_only(self):
        diffs = diff(self.new, self.existing, y_only=True)
        self.assertEqual(len(diffs), 7)

    @Timer.decorator
    def test_diff_list_duplicates(self):
        diffs = diff(self.new, self.existing, duplicates=True)
        self.assertEqual(len(diffs), 2)


if __name__ == '__main__':
    unittest.main()
