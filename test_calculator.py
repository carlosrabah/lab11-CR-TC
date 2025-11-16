import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2,3), 6)
        self.assertEqual(multiply(-4, 5), -20)
        self.assertEqual(multiply(0, 1000), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(9, 3), 3)
        self.assertAlmostEqual(divide(15, 4), 3.75)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

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