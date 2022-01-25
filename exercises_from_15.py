"""
15. Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?


"""

from math import factorial
import string
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

def letters_counter():

    number_to_letters = {i:0 for i in range(1,1001)}

    number_to_letters[1] = 3 #'one',
    number_to_letters[2] = 3 #'two',
    number_to_letters[3] = 5 #three',
    number_to_letters[4] = 4 #'four',
    number_to_letters[5] = 4 #'five',
    number_to_letters[6] = 3 #'six',
    number_to_letters[7] = 5 #'seven',
    number_to_letters[8] = 5 #'eight',
    number_to_letters[9] = 4 #'nine',
    number_to_letters[10] = 3 #'ten',
    number_to_letters[11] = 6 #'eleven',
    number_to_letters[12] = 6 #'twelve',
    number_to_letters[13] = 10 #'thirteenth',
    number_to_letters[14] = 10 #'fourteenth',
    number_to_letters[15] = 9 #'fifteenth',
    number_to_letters[16] = 9 #'sixteenth',
    number_to_letters[17] = 11 #'seventeenth',
    number_to_letters[18] = 10 #'eighteenth',
    number_to_letters[19] = 10 #'nineteenth',
    number_to_letters[20] = 6 #'twenty',
    number_to_letters[30] = 6 #'twenty',
    number_to_letters[40] = 6 #'twenty',
    number_to_letters[50] = 6 #'twenty',
    number_to_letters[60] = 6 #'twenty',
    number_to_letters[70] = 6 #'twenty',
    number_to_letters[80] = 6 #'twenty',
    number_to_letters[90] = 6 #'twenty',
    number_to_letters[1000] = 11 #one thousand 

    for num in range(20,100):
        unit = int(str(num)[1])
        if unit != 0 :
            decimal = int(str(num)[0] + "0")
            number_to_letters[num] = number_to_letters[decimal] + number_to_letters[unit]

    for num in range(100, 1000):
        hundredth = int(str(num)[0])
        if str(num)[1:] == "00":
            # hundred (7)
            number_to_letters[num] =  number_to_letters[hundredth] + 7
        else:
            # and hundred (10)
            decimal = int(str(num)[1:])
            number_to_letters[num] = number_to_letters[hundredth] + 10 + number_to_letters[decimal] 

    sum_of_all_letters = sum(list(number_to_letters.values())) 
    print(sum_of_all_letters)   


#letters_counter()

"""


By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                       75
                      95 64
                     17 47 82
                   18 35 87 10
                  20 04 82 47 65
                19 01 23 75 03 34
               88 02 77 73 07 63 67
             99 65 04 28 06 16 70 92
           41 41 26 56 83 40 80 70 33
         41 48 72 33 47 32 37 16 94 29
       53 71 44 65 25 43 91 52 97 51 14
     70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

"""

def maximum_path_sum_I(string_triangle):
    maximum_path_elements = []
    list_of_elements = [item.strip() for item in string_triangle.split(",")]
    maximum_path_elements.append((int(list_of_elements.pop(0)),0))
    for row in list_of_elements:
        list_of_numbers = list(map(int,row.split(" ")))
        """
        the idea so far, is extract all the numbers in tuples (number-value, list-index-value)
        and extract the 2 index closes to the previous index of the last row, and search for
        the maxium value between the two tuples.
        """
        print(list_of_numbers)
        

maximum_path_sum_I("3,\
                    7 4,\
                    2 4 6,\
                    8 5 9 3")
