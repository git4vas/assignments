def is_prime(n):
    """
    Checks if n is a prime number
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_list(n):
    """
    Makes the list of primes up to n
    """
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

print(prime_list(int(input("Up to which number do you want all prime numbers? "))))