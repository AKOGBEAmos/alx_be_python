# Test cases to check operation performed by the calculator
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(3.2, 1), 4.2)

    def test_subtraction(self):
        """ Test the subtraction method. """
        self.assertEqual(self.calc.subtract(3,1), 2)
        self.assertEqual(self.calc.subtract(0,5), -5)
        self.assertEqual(self.calc.subtract(-3,-6), 3)
    
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 2.0), 0.0)
        self.assertEqual(self.calc.multiply(3.2, -2.0), -6.4)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(5, 5), 1.0)
        self.assertEqual(self.calc.divide(3, 0), None)
        self.assertEqual(self.calc.divide(6.4, 2), 3.2)

if __name__ == "__main__":
  unittest.main()