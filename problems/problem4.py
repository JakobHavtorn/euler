"""Largest palindrome product

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


MIN_VAL = 100
MAX_VAL = 999


def reverse(number):
    return int(str(number)[::-1])


def is_palindrome(number):
    return number == reverse(number)


def largest_palindrome_naive():
    """
    Loop over all possible combinations of a and b.
    Check if their product is a larger palindrome than the last.
    NOTE Finds all palindromes
    """
    largest_palindrome = 0
    palindromes = []
    a = MIN_VAL
    while a < MAX_VAL:
        b = MIN_VAL
        while b <= MAX_VAL:
            if is_palindrome(a * b) and a * b > largest_palindrome:
                largest_palindrome = a * b
                palindromes.append((largest_palindrome, a, b))

            b += 1
        a += 1
    return palindromes


def largest_palindrome_less_naive():
    """Don't repeat evaluations like (a=x1 b=x2) and (a=x2, b=x1).
    NOTE Roughly halves the number of iterations needed compared to `largest_palindrome_naive`.
    NOTE Finds all palindromes.
    """
    largest_palindrome = 0
    palindromes = []
    a = MIN_VAL
    while a < MAX_VAL:
        b = a  # Start b from the value of a to avoid duplicate checks
        while b <= MAX_VAL:
            if is_palindrome(a * b) and a * b > largest_palindrome:
                largest_palindrome = a * b
                palindromes.append((largest_palindrome, a, b))

            b += 1
        a += 1
    return palindromes


def largest_palindrome_count_down():
    """Count down from MAX to MIN to likely find largest palindrome faster.
    NOTE Much faster than the above
    NOTE Does not find all palindromes
    """
    largest_palindrome = 0
    palindromes = []
    a = MAX_VAL
    while a >= MIN_VAL:
        b = MAX_VAL
        while b >= a:  # Stop b at the value of a to avoid duplicate checks
            if a * b <= largest_palindrome:
                break

            if is_palindrome(a * b):
                largest_palindrome = a * b
                palindromes.append((largest_palindrome, a, b))

            b -= 1
        a -= 1
    return palindromes


def largest_palindrome_prime_factor():
    """
    Consider the digits of P: Let them be x, y and z.
    P must be at least 6 digits long since the palindrome 111111 = 143×777 – the product of two 3-digit integers.

    Since P is palindromic, we can factor it as follows:
        P = 100000x + 10000y + 1000z + 100z + 10y + x
        P = 100001x + 10010y + 1100z
        P = 11 * (9091x + 910y + 100z)

    Since 11 is prime, this is a prime factorization. This means that at least one of the integers a or b must have a
    factor of 11. So if a is not divisible by 11 then we know b must be (and the other way around).

    Using this information we can determine what values of b we check depending on a and decrememt b faster.
    """
    largest_palindrome = 0
    palindromes = []
    a = MAX_VAL
    while a >= MIN_VAL:
        if a % 11 == 0:
            b = MAX_VAL
            dec_b = 1
        else:
            b = MAX_VAL - MAX_VAL % 11  # Largest number smaller than or equal to MAX_VAL and divisible by 11
            dec_b = 11

        while b >= a:  # Stop b at the value of a to avoid duplicate checks
            if a * b <= largest_palindrome:
                break

            if is_palindrome(a * b):
                largest_palindrome = a * b
                palindromes.append((largest_palindrome, a, b))

            b -= dec_b
        a -= 1
    return palindromes


if __name__ == '__main__':
    print(reverse(12345))

    palindromes = largest_palindrome_naive()
    for p, a, b in palindromes:
        print(p, a, b)
    print()

    palindromes = largest_palindrome_less_naive()
    for p, a, b in palindromes:
        print(p, a, b)
    print()

    palindromes = largest_palindrome_count_down()
    for p, a, b in palindromes:
        print(p, a, b)
    print()

    palindromes = largest_palindrome_prime_factor()
    for p, a, b in palindromes:
        print(p, a, b)
    print()
