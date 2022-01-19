"""
15. Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?


"""

from math import factorial
import time
 
def main():
    """Main Program"""
    start_time = time.time()
 
    n = 40      # The total number of moves for any one path (right + down)
    r = 20      # The total number of right moves for any one path
 
    print(factorial(n) / (factorial(r) * factorial(n - r)))
    print("Elapsed Time:", (time.time() - start_time) * 1000, "millisecs")
 
# if __name__ == '__main__':
#     main()

"""
16. 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""
import functools

def sum_of_digits(power_number):
    string_representation = str(pow(2,power_number))
    print(functools.reduce(lambda a, b: int(a) + int(b), string_representation))

#sum_of_digits(1000)

"""
17. If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
 how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.

"""

number_to_letters = {
    1 : 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteenth',
    14: 'fourteenth',
    15: 'fifteenth',
    16: 'sixteenth',
    17: 'seventeenth',
    18: 'eighteenth',
    19: 'nineteenth',
    20: 'twenty',
    

}



