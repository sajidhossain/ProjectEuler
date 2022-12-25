"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiplies(n):
    if n % 3 == 0 or n % 5 == 0:
        return n
    else:
        return 0


summation = 0
for i in range(3, 1000):
    summation = summation + multiplies(i)
print(summation)
