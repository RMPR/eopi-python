"""
A natural number is called a prime if it is bigger than
1 and has no
divisors other than
1 and itself.
Write a program that takes an integer argument and retums all the primes between 1 and that
integer. For example, if the input is 18, you should retum <2,3,5,7,77,13,\7>.
"""
from math import sqrt


def primes(n: int):
    """The sieve of Erasthostene. """
    if n < 2:
        return []
    is_prime: list[bool] = [False, False] + [True] * (n - 1)
    for i in range(2, int(sqrt(n + 1)) + 1):
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return [i for i, j in enumerate(is_prime) if j]


if __name__ == "__main__":
    assert(primes(18) == [2, 3, 5, 7, 11, 13, 17])
    assert(primes(1) == [])
    assert(primes(2) == [2])
    assert(primes(7) == [2, 3, 5, 7])
