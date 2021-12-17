"""
9. A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
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

#print(pythagorean_triplet())

"""
10. The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def sum_of_primes(upper_boundary):
    acc = 2 + 3
    for iter in range(4,upper_boundary):
        for i in range(2,iter + 1):
            if (iter%i==0 and iter != i):
                break
            elif i == iter:
                acc = acc + iter
    return acc

#print(sum_of_primes(2000000))
import math

def sum_of_primes_best(upper_boundary):    
    
    def primecheck(num):
        divisor = 3
        sqrt_divided = int(math.sqrt(num))
        while divisor <= sqrt_divided:
            if num % divisor == 0:
                return False
            divisor += 2
        return True

    primesum = sum([2] + [x for x in range(3,upper_boundary + 1,2) if primecheck(x)])
    
    print("Result: ",primesum)


print(sum_of_primes_best(2000000))
