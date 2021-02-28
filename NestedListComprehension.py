# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 11:01:13 2020

@author: Michael
"""

"""

input: empty list
output: list within a list

"""

matrix = [] # create an empty list

for i in range(5): # iterate from 0 to 4
    matrix.append([]) # append an empty list inside matrix list

    for j in range(5): # iterate from 0 to 4
        matrix[i].append(j) # populate matrix[i] (a list) with values from 0 to 4
        # once j = 4, then go back to for i in range(5) and start again
        
print(f"\nThis is matrix_1:\n{matrix}\n")
    
matrix_2 = [[j for j in range(5)] for i in range(5)]

print(f"This is matrix_2:\n{matrix_2}\n")

#matrix_3 = [[1,2,3], [4,5], [6,7,8,9]]

flatten_matrix = []

for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)
        
print(f"This is the flattened matrix:\n{flatten_matrix}\n")

flatten_matrix_list = [val for sublist in matrix for val in sublist]

print(f"this is the flattened matrix by list:\n{flatten_matrix_list}")








