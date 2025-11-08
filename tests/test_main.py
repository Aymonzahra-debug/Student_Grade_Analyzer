import unittest
import os

class TestStudentGradeAnalyzer(unittest.TestCase):
    def test_data_file_exists(self):
        """Check that the students.npy file exists."""
        self.assertTrue(os.path.exists("students.npy"), "students.npy file is missing")

    def test_math(self):
        """Simple test to make sure CI is running."""
        self.assertEqual(2 + 3, 5)

if __name__ == "__main__":
    unittest.main()
