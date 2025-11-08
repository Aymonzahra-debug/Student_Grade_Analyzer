import unittest
import os
import main  # import your main.py file

class TestStudentGradeAnalyzer(unittest.TestCase):
    def test_data_file_exists(self):
        """Check that the students.npy file exists."""
        self.assertTrue(os.path.exists("students.npy"), "students.npy file is missing")

    def test_math(self):
        """Simple test to make sure CI is running."""
        self.assertEqual(2 + 3, 5)

class TestGradeCalculations(unittest.TestCase):
    def test_average_grade(self):
        """Check that average grade calculation works correctly."""
        grades = [80, 90, 100]
        expected = 90
        result = main.calculate_average(grades)
        self.assertEqual(result, expected, "Average grade calculation is incorrect")

if __name__ == "__main__":
    unittest.main()
