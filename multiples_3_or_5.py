"""
1. If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_multiples_3_or_5(upper_threshold):
    acc = 0
    for i in range(upper_threshold):
        if i % 3 == 0 or i % 5 == 0:
            acc = acc + i
    return acc

#print(sum_multiples_3_or_5(10))    

"""
2. Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def sum_even_fibonacci_numbers(upper_thresold):
    fibonnaci_values = [1,2]
    total_sum = 2
    while fibonnaci_values[-2] + fibonnaci_values[-1] < upper_thresold:
        fibonnaci_values.append(fibonnaci_values[-2] + fibonnaci_values[-1])
        if fibonnaci_values[-1] % 2 == 0:
            total_sum = total_sum + fibonnaci_values[-1]

    return total_sum        

#print(sum_even_fibonacci_numbers(100))

"""
3. The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
#my try:
def largest_prime_factor(target_number, iter=1, prime_numbers = [2,3], prime_factors = []):
    prime_numbers.append(6*iter - 1)
    prime_numbers.append(6*iter + 1)

    if target_number == 1:
        return max(prime_numbers)
    for prime_number in prime_numbers:
        if target_number % prime_number == 0:
            prime_factors.append(prime_number)
            largest_prime_factor(target_number / prime_number, iter = iter + 1, prime_numbers = prime_numbers, prime_factors = prime_factors)

#some internet answer
def max_factor(num):
    """Find the maximum prime factor."""
    factor = 2
    while factor * factor <= num:
        while num % factor == 0:
            #we must to divide, and re asigns this divided value to the num variable
            num /= factor
        factor += 1
    if (num > 1):
        return num
    return factor

#print(max_factor(13195))

"""
4. A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
from itertools import permutations, combinations

def found_palindromic():
    comb = combinations(list(range(100)),2)
    max = 0
    for pairs in comb:
        product = pairs[0] * pairs[1]   
        if str(product) == str(product)[::-1]:
            max = product
    return max        

#print(found_palindromic())

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
#my version
def smallest_multiple():
    smallest_number = 1
    while True:
        for i in range(1,21):
            print(smallest_number % i, i, smallest_number)
            if smallest_number % i == 0:
                if i == 20:
                    return smallest_number
                else:
                    continue    
            else:
                break    
        
        smallest_number += 1

#print(smallest_multiple())
#version find it on stack overflow
import functools
import math

def smallest_multiple_best():
    return functools.reduce(lambda x,y: x*y//math.gcd(x, y), range(1, 21))

print(smallest_multiple_best())





