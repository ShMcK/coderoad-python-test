import unittest
import sys
sys.path.append('./coderoad/src')

from example import add


class MathTest(unittest.TestCase):
    def test_add_no_numbers(self):
        self.assertEqual(add(), 0, "Should return 0 with no params")
    def test_add_one_number(self):
        self.assertEqual(add(1), 1, "Should add one number to 0")
    def test_add_two_numbers(self):
        self.assertEqual(add(1, 2), 3, "Should add two numbers together")
    def test_add_three_numbers(self):
        self.assertEqual(add(1, 2, 3), 6, "Should add three numbers together")

if __name__ == '__main__':
    unittest.main()