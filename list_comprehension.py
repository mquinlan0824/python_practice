# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:43:34 2021

@author: Michael Q
"""

students = [
    ['Harry', 3.5, 3, True],
    ['Ron', 2.7, 2, True],
    ['Hermione', 3.9, 1, False],
    ['Dumbeldore', 2.9, 4, True],
    ['Snape', 3.1, 4, False],
]


# Ex_1: Use list comprehension to extract student names from list
'''
input: students list
identify students in list by name
output: student name
'''
names = [student[0] for student in students]
print(names)

# Ex_2: Use list comprehension to extract the length of each student's name
'''
input: list of students
count number of characters in student name
output: length of each student's name
'''
length_names =[len(student[0]) for student in students]
print(length_names)

# Ex_3: Using criteria to get the name of every 4th year student
'''
input: student list of data
criteria: identify fourth year students
output: name of every 4th year student
'''
fourth_year_not = [student[0] for student in students if (student[2] != 4)]
print(fourth_year_not)

# Ex_4: Using criteria to get every fourth year or in-state student
'''
input: student list
criteria: identify fourth year and in-state students
output: student name that meets criteria
'''
fourth_instate = [student[0] for student in students if (student[2] == 4) or (student[3] == True)]
fourth_instate

# Ex_5: Use nested list comprehension: get data type of each piece of data in list
'''
input: student list
extract data type of each element in list
output: data type
'''
data_type = [[type(item) for item in student] for student in students]
data_type

# Ex_6: Use nested listed comprehension to gte the square of each even integer between 2 and 10
square_numbers = [x**2  for x in range(1, 11) if (x % 2 == 0)]
square_numbers

'''
alternative solution:
square_numbers = [i**2 for i in range(2, 11, 2)]
range function takes start and end (exclusive) and steps by 2
2, 4, 6, 8, 10
'''

# Ex_7: Use list comprehension to 'flatten' a matrix
'''
input: 3x3 matrix of values
extract every item from matrix and store in list
output: 1x9 matrix of values [a list of nine values]
'''
M = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list = []
flatten_list = [item for row in M for item in row]

'''
A for loop might be better in this situation because it is easier to understand
'''

flatten_list = []
for list in M:
    for item in list:
        flatten_list.append(item)

# Ex_8: Time considerations
'''
quick experiment to compare time cost for list comprehension v. for loop
in jupyter notebook, you can use %%timeit to track time and std of time to run
'''






