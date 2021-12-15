"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def pythagorean_triplet():
    sum_value = 1000
    for a in range(1, sum_value//3):
        for b in range(1, sum_value//2):
            b = b + a + 1
            c = sum_value - b - a
            if a*a + b*b == c*c:
                print(a,b,c)
                return a * b * c

print(pythagorean_triplet())