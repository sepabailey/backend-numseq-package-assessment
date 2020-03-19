def primes(n):
    """
    Returns a list of all prime numbers less than n
    """

    prime_list = [2, 3, 5, 7]
    if n <= 1:
        return []
    for i in range(10, n, 10):
        for digit in (1, 3, 7, 9):
            if is_prime(i + digit):
                prime_list.append(i + digit)
    return prime_list


def is_prime(m):
    """
    Returns a boolean indicating whether `m` is a prime number
    """

    if m == 2 or m == 3:
        return True
    if m % 2 == 0 or m < 2:
        return False
    for i in range(3, int(m**0.5) + 1, 2):
        if m % i == 0:
            return False
    return True
