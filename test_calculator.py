import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(-9, -5), -14)
        self.assertEqual(self.calc.add(-5, 8), 3)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(-10, 20), -30)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()