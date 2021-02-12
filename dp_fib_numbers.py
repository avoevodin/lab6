'''Generate Fibonacci numbers.

'''
def fib_rec(num):
    '''Generate Fibonacci numbers with recursion.
    Big amount calls of recursion. Mustn't use.

    '''
    if num <= 1:
        return num
    return fib(num-1) + fib(num-2)

def fib(num):
    '''Generate Fibonacci numbers with dynamic programming.

    Keyword arguments:
    n -- argument for Fibonacci function (int)

    '''
    fib_n = [0, 1] + [0] * (num - 1)
    for i in range(2, num + 1):
        fib_n[i] = fib_n[i - 1] + fib_n[i - 2]
    return fib_n

def test_fib():
    '''Common tests for Fibonacci numbers.

    '''
    num = 4
    fib_n = [0, 1, 1, 2, 3]
    test_case_fib(num, fib_n, "1")

    num = 6
    fib_n = [0, 1, 1, 2, 3, 5, 8]
    test_case_fib(num, fib_n, "1")

    num = 9
    fib_n = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    test_case_fib(num, fib_n, "1")

def test_case_fib(num, fib_n, case_name):
    '''Test case for Fibonacci numbers.

    '''
    print("testcase #", case_name, ": ", end="")
    fib_n_counted = fib(num)
    print("Ok" if fib_n == fib_n_counted else "Fail", fib_n_counted, sep=": ")

if __name__ == '__main__':
    test_fib()
