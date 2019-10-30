"""
A natural number is called a prime if it is bigger than 1 and has no divisors
other than 1 and itself.

Write a program that takes an integer argument and returns all the primes
between 1 and that integer. For example, if the input is 18, you should return
<2,3,5,7,11,13,17>.

Hint: Exclude the multiples of primes.

"""

def generate_primes(n):
    """
    Space complexity: O(n)
    Time complexity: O(nloglogn)

    """

    primes = []
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes

def generate_primes(n):
    """
    Space complexity: O(n)
    Time complexity: O(nloglogn)

    """

    if n < 2:
        return []
    size = (n - 3) // 2 + 1
    primes = [2]
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False
    return primes
