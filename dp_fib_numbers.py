"""Generate Fibonacci numbers.

"""
import unittest


def fib_rec(num):
    """Generate Fibonacci numbers with recursion.
    Big amount calls of recursion. Mustn't use.

    """
    if num <= 1:
        return num
    return fib_rec(num - 1) + fib_rec(num - 2)


def fib(num):
    """Generate Fibonacci numbers with dynamic programming.

    Keyword arguments:
    n -- argument for Fibonacci function (int)

    """
    fib_n = [0, 1] + [0] * (num - 1)
    for i in range(2, num + 1):
        fib_n[i] = fib_n[i - 1] + fib_n[i - 2]
    return fib_n


if __name__ == '__main__':
    unittest.main(verbosity=2, module='test_fib_numbers')
