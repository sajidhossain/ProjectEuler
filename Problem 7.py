from math import sqrt


def prime_check(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
            break
    return True


prime = [2]
i = 3
while True:
    if len(prime) < 10001:
        if prime_check(i):
            prime.append(i)
    else:
        break
    i += 2
print(prime[-1])