"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 2
    if number_of_primes <= 0:
        raise ValueError
    while len(list) < number_of_primes:
        isPrime = True
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
        if isPrime:
            list.append(num)
        num += 1
    return list
