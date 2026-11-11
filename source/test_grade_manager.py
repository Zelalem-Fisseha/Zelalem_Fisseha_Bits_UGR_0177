# Unit tests for the calculation part of grade_manager.py
# (test cases TC01 - TC06 in the test table). Run with:
#   python -m unittest test_grade_manager.py

import unittest

from grade_manager import calculate_average, letter_grade


class TestCalculations(unittest.TestCase):

    def test_tc01_average(self):
        self.assertEqual(calculate_average([80, 90, 70]), 80.00)

    def test_tc02_boundary_a_plus(self):
        self.assertEqual(letter_grade(90), ("A+", 4.00))

    def test_tc03_just_below_boundary(self):
        self.assertEqual(letter_grade(89.99), ("A", 4.00))

    def test_tc04_lowest_pass(self):
        self.assertEqual(letter_grade(40), ("D", 1.00))

    def test_tc05_fail(self):
        self.assertEqual(letter_grade(39.5), ("F", 0.00))

    def test_tc06_limits(self):
        self.assertEqual(letter_grade(100), ("A+", 4.00))
        self.assertEqual(letter_grade(0), ("F", 0.00))


if __name__ == "__main__":
    unittest.main()
