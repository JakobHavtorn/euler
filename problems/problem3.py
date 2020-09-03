"""Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

import math
import numpy as np


def largest_prime_factor_naive(number):
    """
    Let the given number be n and let k = 2, 3, 4, 5, ... .

    For each k, if it is a factor of n then we divide n by k and completely divide out each k before moving to the next k.

    It can be seen that when k is a factor it will necessarily be prime, as all smaller factors have been removed,
    and the final result of this process will be n = 1.
    """
    factor = 2
    factors = []
    while number > 1:
        if number % factor == 0:
            factors.append(factor)
            number = number // factor  # Remainder guarenteed to be zero
            while number % factor == 0:
                number = number // factor  # Remainder guarenteed to be zero
        factor += 1
    return factors


def largest_prime_factor_even_optimized(number):
    """
    We know that, excluding 2, there are no even prime numbers.
    So we can increase factor by 2 per iteration after having found the 
    """
    factors = []
    factor = 2
    if number % factor == 0:
        number = number // factor
        factors.append(factor)
        while number % factor == 0:
            number = number // factor

    factor = 3
    while number > 1:
        if number % factor == 0:
            factors.append(factor)
            number = number // factor  # Remainder guarenteed to be zero
            while number % factor == 0:
                number = number // factor  # Remainder guarenteed to be zero
        factor += 2
    return factors


def largest_prime_factor_square_optimized(number):
    """
    Every number n can at most have one prime factor greater than n.

    If we, after dividing out some prime factor, calculate the square root of the remaining number
    we can use that square root as upper limit for factor.
    
    If factor exceeds this square root we know the remaining number is prime.
    """
    factors = []
    factor = 2
    if number % factor == 0:
        number = number // factor
        factors.append(factor)
        while number % factor == 0:
            number = number // factor

    factor = 3
    max_factor = math.sqrt(number)
    while number > 1 and factor <= max_factor:
        if number % factor == 0:
            factors.append(factor)
            number = number // factor
            while number % factor == 0:
                number = number // factor
                max_factor = math.sqrt(number)
        factor += 2

    return factors


def idx_sieve(length):
    """Static length sieve-based prime generator"""
    primes = []
    is_prime = np.array([True]*length)
    i = 2
    while i < length:
        if is_prime[i]:
            is_prime[np.arange(i, length, i)] = False
            primes.append(i)
        else:
            i += 1
    return primes


def prime_factor(n, primes):
    i = 0
    factors = []
    while n != 1:
        while (n % primes[i]) != 0:
            i += 1
        factors.append(primes[i])
        n = n / primes[i]
    return factors


if __name__ == '__main__':
    number = 600851475143
    print(largest_prime_factor_naive(number))
    print(largest_prime_factor_even_optimized(number))
    print(largest_prime_factor_square_optimized(number))

    number = 600851475143
    primes = idx_sieve(20000)
    
    print(max(prime_factor(number, primes)))
