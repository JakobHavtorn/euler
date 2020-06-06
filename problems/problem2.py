"""Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""

import logging
import timeit

from utils import FORMAT


logging.basicConfig(format=FORMAT, level=logging.INFO)
LOGGER = logging.getLogger()


def brute_force(limit=4e6):
    s = 0
    prevprev = 1
    prev = 1
    while prev < limit:
        if prev % 2 == 0:
            s = s + prev
        new = prevprev + prev
        prevprev = prev
        prev = new
    return s


def ignore_odd(limit=4e6):
    """Exploit that every third fibonacci number is even"""
    s = 0
    prevprev = 1
    prev = 1
    while prev < limit:
        if prev % 2 == 0:
            s = s + prev
        new = prevprev + prev
        prevprev = prev
        prev = new
    return s


def recursive_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib = recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
    return fib


efficient_sum = 0
def efficient_recursion(limit=4e6):
    """Exploit the recursion F(n)=4*F(n-3)+F(n-6) for the even Fibonaccis"""
    pass


if __name__ == '__main__':
    s = brute_force()
    LOGGER.info('brute_force: %s', s)

    s = ignore_odd(limit=4e6)
    LOGGER.info('ignore_odd: %s', s)
