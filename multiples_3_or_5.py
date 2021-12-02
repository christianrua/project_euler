"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""

def sum_multiples_3_or_5(upper_threshold):
    acc = 0
    for i in range(upper_threshold):
        if i % 3 == 0 or i % 5 == 0:
            acc = acc + i
    return acc

print(sum_multiples_3_or_5(10))             
