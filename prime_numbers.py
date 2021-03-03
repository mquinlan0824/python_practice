# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:58:34 2021

@author: Michael Quinlan

"""
'''
input: interger
output: list of factors
The goal of this script is to find the prime factors of an integer
'''

prime_factor_list =[] # create an empty list to store factors
def prime_factor(x):
    for i in range(1, x +1): # iterate over range of input integer
        if x == 2: # if input number is equal to 2
            prime_factor_list.append(int(x)) # append to list
            break # end
        elif (x%i == 0): # if remainder of integer divided by interator is 0
            prime_factor_list.append(int(i)) # add iterator to list of factors
            x = (x / i) # divide integer by iterator and continue
    return prime_factor_list

integer = int(11)
prime_factor_list = prime_factor(integer)
print(prime_factor_list)