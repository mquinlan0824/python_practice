# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:02:37 2020

@author: Asus
"""

"""
Using the Universal Soil Loss Equation
"""
import math

# program to calculate the s factor in the USLE 

slope = input("Enter the slope in degrees: ")
slopeFloat=float(slope)
if float(slope) < 0.0 or float(slope) > 45:
    print("You have entered an invalid slope value.")
    slope = input("Enter a value greater than 0 or less than 45 degrees: ")

print("The slope you entered is", slope, "degrees.")

if float(slope) < 0.0 or float(slope) > 45:
    print("You have entered an invalid slope value.")
    slope = input("Enter a value greater than 0 or less than 45 degrees: ")

# slope in radians
slopeRadians = (slopeFloat/360) * 2.0 * math.pi
print("This corresponds to a slope of ", slopeRadians, "in radians.")

# slope in m/m
slopeFraction = math.tan(slopeRadians)
print("This corresponds to a slope of ", slopeFraction, "(m/m)")

# slope factor
S = 0.065 + 0.045 * slopeFraction + 0.0065 * slopeFraction**2.0

print("The slope factor is", S)