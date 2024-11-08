import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
    # Add the following test methods to the TestCalculator class:
    def test_add(self):
        self.assertEqual(self.calc.add(-9, -5), -14)
    def test_add2(self):
        self.assertEqual(self.calc.add(-5, 8), 3)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(-10, 20), -30)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(-10, -20), 10)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-10, -20), 200)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(-10, 0), 0)
    def test_divide(self):
        self.assertEqual(self.calc.divide(-10, -20), 0)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(-10, 0), 0)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(9, 9), 0)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(-10, -20), -10)

if __name__ == '__main__':
    unittest.main()