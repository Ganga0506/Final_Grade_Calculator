import unittest
from grade_calculator import calculate_grade

class TestGradeCalculator(unittest.TestCase):
    def test_single_assignments(self):
        # Test a single assignment with 100% weight
        assignments = [("Assignments 1", 90, 100)]
        self.assertEqual(calculate_grade(assignments), 90)

    def test_multiple_assignments(self):
        # Test multiple assignments with valid scores and weights
        assignments = [
            ("Classwork", 90, 15),
            ("Projects", 85, 20),
            ("Exams", 70, 30),
            ("Homework", 88, 35)
        ]
        # Expected final grade based on weighted average
        expected = (90 * .15 + 85 * .20 + 70 * .30 + 88 * .35)
        self.assertEqual(calculate_grade(assignments), expected)

    def test_no_assignments(self):
        # Test when no assignments are given
        assignments = []
        self.assertEqual(calculate_grade(assignments), 0)

if __name__ == "__main__":
    unittest.main()