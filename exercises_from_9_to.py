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

from multiples_3_or_5 import largest_prime_factor

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


#print(sum_of_primes_best(2000000))
"""
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

"""
import math

class GridMatrixFunctions:

    def __init__(self, text_grid):
        self._text_grid = text_grid

    def prod_of_rows(self, matrix, max_value_dict):
        """
            This function sums all the elements for a row
        """

        for iterator in range(0,len(matrix)):
            if math.prod(matrix[iterator][0]) > max_value_dict["prod_max_value"]:
                max_value_dict["prod_max_value"] = math.prod(matrix[iterator][0]) #sum(matrix[iterator][0])
                max_value_dict["list_of_numbers_max_value"] = matrix[iterator][0]

        return max_value_dict

    def prod_of_columns(self, matrix, max_value_dict):
        """
            This function is for sum all values inside each column
        """

        for iterator in range(0, len(matrix)):
            col_list = [matrix[0][0][iterator],matrix[1][0][iterator],matrix[2][0][iterator],matrix[3][0][iterator]]
            col_list_sum_value = math.prod(col_list)
            if col_list_sum_value > max_value_dict["prod_max_value"]:
                max_value_dict["prod_max_value"] = col_list_sum_value
                max_value_dict["list_of_numbers_max_value"] =  col_list

        return max_value_dict        

    def prod_diagonally_cols(self, matrix, max_value_dict):
        
        max_value = max_value_dict["prod_max_value"]
        right_diagonally = [matrix[0][0][0],matrix[1][0][1],matrix[2][0][2],matrix[3][0][3]]
        left_diagonally = [matrix[0][0][3],matrix[1][0][2],matrix[2][0][1],matrix[3][0][0]]

        max_value_left = math.prod(left_diagonally)
        max_value_right = math.prod(right_diagonally)

        if max_value_left > max_value_right and max_value_left > max_value:
            max_value_dict = {
                "prod_max_value":max_value_left,
                "list_of_numbers_max_value":left_diagonally
            }
            return max_value_dict
        elif max_value_right > max_value_left and max_value_right > max_value:
            max_value_dict = {
                "prod_max_value":max_value_right,
                "list_of_numbers_max_value":right_diagonally
            }
            return max_value_dict    
        else:
            return max_value_dict     


    def parse_matrix(self):
        """
            This function cast the string matrix, to a int matrix
        """
        raw_grid = list(filter(lambda x: x != '',self._text_grid.split(" ")))
        int_list = list(map(int, raw_grid))
        arrays_by_20 = []
        for lower_index in range(0,400,20):
            arrays_by_20.append(int_list[lower_index:lower_index+20])
        return arrays_by_20

    def matrix_operations(self, matrix):
        """
            This function is used to apply all the different operations in the received matrix
        """
        sum_value = self._prod_of_rows(matrix)
        return sum_value

def largest_product_in_a_grid(grid):
    # the first step is to cast the string to a matrix format
    grid_helper = GridMatrixFunctions(grid)
    matrix_20_by_20 = grid_helper.parse_matrix()
    biggest_product = 0

    max_prod_rows_value = {
                "prod_max_value":0,
                "list_of_numbers_max_value":[]
            }

    max_prod_cols_value = {
                "prod_max_value":0,
                "list_of_numbers_max_value":[]
            }

    max_prod_diagnolity_value = {
                "prod_max_value":0,
                "list_of_numbers_max_value":[]
            }
    #print(matrix_20_by_20)
    #the next step is to traverse the matrix by row.
    for row in range(0,len(matrix_20_by_20),4):
        row1 = matrix_20_by_20[row]
        row2 = matrix_20_by_20[row + 1]
        row3 = matrix_20_by_20[row + 2]
        row4 = matrix_20_by_20[row + 3]

        print("iter---------------------")    
        for column in range(0, len(matrix_20_by_20)):
            if column + 3 == len(matrix_20_by_20):
                break
            
            local_matrix = [
                            [row1[column:column+4]],
                            [row2[column:column+4]],
                            [row3[column:column+4]],
                            [row4[column:column+4]]
                            ]
            #this is the part where you find the max value, when do prod on all the rows                
            print("*******************************")
            local_max_row_value = grid_helper.prod_of_rows(local_matrix,max_prod_rows_value)
            max_prod_rows_value = local_max_row_value 
            print("rows prod value",local_max_row_value)  

            
            local_max_colum_value = grid_helper.prod_of_columns(local_matrix,max_prod_cols_value)
            max_prod_cols_value = local_max_colum_value
            print("columns prod value",local_max_colum_value)  

            
            local_max_diagnolaty_value = grid_helper.prod_diagonally_cols(local_matrix,max_prod_diagnolity_value)
            max_prod_diagnolity_value = local_max_diagnolaty_value
            print("diagnolaty_prod value",local_max_diagnolaty_value)  
            print("********************************")

                 

largest_product_in_a_grid("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\
                            49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\
                            81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\
                            52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\
                            22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\
                            24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\
                            32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\
                            67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\
                            24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\
                            21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\
                            78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\
                            16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\
                            86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\
                            19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\
                            04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\
                            88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\
                            04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\
                            20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\
                            20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\
                            01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")