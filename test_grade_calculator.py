import unittest
from grade_calculator import calculate_grade, InvalidWeightError 

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

    
    def test_invalid_grade(self):
        # Test with an invalid score (negative grade)
        assignments = [
            ("Classwork", 90, 15),
            ("Projects", -5, 20),  # Invalid score
            ("Exams", 70, 30),
            ("Homework", 88, 35)
        ]
        # Should raise a custom error for invalid input
        with self.assertRaises(InvalidWeightError):
            calculate_grade(assignments)

    def test_invalid_weights(self):
        # Test with an invalid weight (negative value)
        assignments = [
            ("Classwork", 90, 15),
            ("Projects", 85, -20),  # Invalid weight
            ("Exams", 70, 30),
            ("Homework", 88, 35)
        ]
        # Should raise a custom error for invalid input
        with self.assertRaises(InvalidWeightError):
            calculate_grade(assignments)

    def test_weights_dont_add_up_to_100(self):
        # Test when total weights add up to less than 100
        assignments = [
            ("Quiz", 100, 40),
            ("Midterm", 80, 40)
        ]
        # Normalize the weights to get the correct final grade
        expected = (100*0.4 + 80*0.4) / 0.8
        self.assertAlmostEqual(calculate_grade(assignments), expected)  

    def test_weights_add_up_to_more_than_100(self):
        # Test when total weights add up to more than 100
        assignments = [
            ("Quiz", 100, 50),
            ("Midterm", 80, 60)
        ]
        # Normalize the weights to get the correct final grade
        expected = (100*0.5 + 80*0.6) / 1.1
        self.assertAlmostEqual(calculate_grade(assignments), expected)


if __name__ == "__main__":
    unittest.main()