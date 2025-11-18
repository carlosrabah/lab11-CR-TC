#https://github.com/carlosrabah/lab11-CR-TC.git

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 10), -10)
        self.assertEqual(subtract(-2, -2), 0)

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(-4, 5), -20)
        self.assertEqual(mul(0, 1000), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 5), 2)
        self.assertEqual(div(9, 3), 3)
        self.assertAlmostEqual(div(15, 4), 3.75)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)

if __name__ == "__main__":
    unittest.main()