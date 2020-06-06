"""Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import logging
import timeit

from utils import FORMAT


logging.basicConfig(format=FORMAT, level=logging.INFO)
LOGGER = logging.getLogger()


def brute_force(target):
    summ = 0
    for i in range(target):
        if i % 3 == 0 or i % 5 == 0:
            summ += i
    return summ


def sum_divisible_by_n(target, n):
    """
    Note that for 5: 5+10+15+...+995 = 5*(1+2+....+199)
    Also note:       1+2+3+...+p = ½*p*(p+1)
    """
    p = target // n
    return n * (p * (p + 1)) // 2


def include_exclude(target):
    return sum_divisible_by_n(target, 3) + sum_divisible_by_n(target, 5) - sum_divisible_by_n(target, 15)


if __name__ == '__main__':
    s = brute_force(target=1000)
    LOGGER.info('brute_force: %s', s)

    s = include_exclude(target=999)
    LOGGER.info('include_exclude: %s', s)
