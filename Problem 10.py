"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def SieveOfEratosthenes(num):
    prime = [True] * num
    primenumber = []
    # boolean array
    p = 2
    while p * p <= num:
        # If prime[p] is not
        # changed, then it is a prime
        if prime[p] == True:
            for i in range(p * p, num, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, num):
        if prime[p]:
            primenumber.append(p)
    return primenumber


print(sum(SieveOfEratosthenes(2000000)))
