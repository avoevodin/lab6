import unittest
from dp_fib_numbers import fib, fib_rec


class FibonacciTestCase(unittest.TestCase):
    def test_case_fib1(self):
        num = 4
        fib_n = [0, 1, 1, 2, 3]
        fib_n_counted = fib(num)
        self.assertEqual(fib_n, fib_n_counted)

    def test_case_fib2(self):
        num = 6
        fib_n = [0, 1, 1, 2, 3, 5, 8]
        fib_n_counted = fib(num)
        self.assertEqual(fib_n, fib_n_counted)

    def test_case_fib3(self):
        num = 9
        fib_n = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        fib_n_counted = fib(num)
        self.assertEqual(fib_n, fib_n_counted)


class FibonacciRecTestCase(unittest.TestCase):
    def test_case_fib_rec1(self):
        num = 4
        fib_n = [0, 1, 1, 2, 3]
        fib_n_counted = [fib_rec(i) for i in range(num+1)]
        self.assertEqual(fib_n, fib_n_counted)

    def test_case_fib_rec2(self):
        num = 6
        fib_n = [0, 1, 1, 2, 3, 5, 8]
        fib_n_counted = [fib_rec(i) for i in range(num+1)]
        self.assertEqual(fib_n, fib_n_counted)

    def test_case_fib_rec3(self):
        num = 9
        fib_n = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        fib_n_counted = [fib_rec(i) for i in range(num+1)]
        self.assertEqual(fib_n, fib_n_counted)
