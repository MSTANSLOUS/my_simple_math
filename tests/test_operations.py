import unittest
from my_simple_math import (
    add,
    subtract,
    multiply,
    divide,
    power,
    factorial,
    is_prime
)

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0.5, 0.25), 0.75)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(10, 10), 0)
        self.assertEqual(subtract(3.5, 1.5), 2.0)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(2.5, 4), 10.0)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-3, -2), 6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(0, 5), 0.0)
        
        # Test division by zero
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(4, 0.5), 2.0)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(2, -1), 0.5)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        
        # Test negative input
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(7919))  # Large prime
        
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(100))
        
        # Test invalid inputs
        with self.assertRaises(ValueError):
            is_prime(1)
        with self.assertRaises(ValueError):
            is_prime(-5)

if __name__ == '__main__':
    unittest.main()
