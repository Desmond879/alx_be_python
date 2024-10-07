# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method of SimpleCalculator."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(3.5, 2.5), 6.0)

    def test_subtraction(self):
        """Test the subtraction method of SimpleCalculator."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-5, 5), -10)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(3.5, 1.5), 2.0)

    def test_multiplication(self):
        """Test the multiplication method of SimpleCalculator."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-5, -5), 25)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(3.5, 2), 7.0)

    def test_division(self):
        """Test the division method of SimpleCalculator."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(0, 1), 0.0)
        self.assertEqual(self.calc.divide(3.5, 0.5), 7.0)

        # Test division by zero
        self.assertIsNone(self.calc.divide(10, 0), "Expected None when dividing by zero")

    def test_division_invalid_input(self):
        """Test the division method for invalid inputs."""
        with self.assertRaises(TypeError):
            self.calc.divide("ten", 2)
        with self.assertRaises(TypeError):
            self.calc.divide(10, "two")
        with self.assertRaises(TypeError):
            self.calc.divide("ten", "two")

if __name__ == "__main__":
    unittest.main()
