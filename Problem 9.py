'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

for n in range(1, 500):
    for m in range(n+1, 500):
        if 2*m*m+2*m*n == 1000:
            p = m*m-n*n
            q = 2*m*n
            r = m*m+n*n
print(p*q*r)
