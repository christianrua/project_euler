"""
Exercise 14.

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been 
proved yet (Collatz Problem),it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

def generate_secuence(numbers_list = []):

    if len(numbers_list) == 1:
        last_number = numbers_list[0]
    else:    
        last_number = numbers_list[-1]

    if last_number == 1:
        return numbers_list
    elif last_number % 2 == 0:
        numbers_list.append(last_number/2)
        generate_secuence(numbers_list)    
    else:
        numbers_list.append(3*last_number + 1)    
        generate_secuence(numbers_list)

    return numbers_list

def find_biggest_chain():

    dic = {n: 0 for n in range(1,1000000)}
    dic[1] = 1
    dic[2] = 2

    actual_number = 3
    iteration_data = {
        "max_length": 0,
        "max_number": 0
    }    

    while actual_number <= 1000000:
        response = len(generate_secuence([actual_number]))

        if response > iteration_data['max_length']:
            iteration_data['max_length'] = response
            iteration_data['max_number']= actual_number
            #print(iteration_data,'\n')
        
        actual_number += 1    

    return iteration_data

#print(find_biggest_chain())    

#http://radiusofcircle.blogspot.com

def find_biggest_chain_best():
    #time module for calculating execution time
    import time

    #time at the start of program execution
    start = time.time()

    #dictionary with all the values initialized to 0
    dic = {n: 0 for n in range(1,1000000)}

    #Entering the values of 1 and 2
    dic[1] = 1
    dic[2] = 2

    #for loop find find the size of collatz sequences
    for n in range(3,1000000,1):
        
        #counter to count the size for each iteration
        counter = 0
        
        #original number
        original_number = n

        #while loop to do collatz iterations
        while n > 1:

            #check if the number is a previous sequence
            if n < original_number:

                #Size of collatz sequence for the iteration
                dic[original_number] = dic[n] + counter
                break

            #collatz sequence conditions
            if n%2 == 0:
                n = n/2
                counter += 1
            else:
                n = 3*n+1
                counter += 1

    #dic.values() will give the values of the dictionary
    #list.index(some_number) will output the index
    #of the number. As the index starts from 0
    #we are adding one to the index.
    print(list(dic.values()).index(max(dic.values())) +1)

    #time at the end of execution
    end = time.time()

    #printing the total time of execution
    print(end - start)

print(find_biggest_chain_best())     