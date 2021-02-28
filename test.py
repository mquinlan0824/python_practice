# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:02:37 2020

@author: Asus
"""

"""
Using the Universal Soil Loss Equation
"""
import math

def degreesToRadians(angleInDegrees):
    angleInRadians = (angleInDegrees / 360.0) * 2.0 * math.pi
    return angleInRadians

print(degreesToRadians(34))
# program to enter the slope in degrees

#slope = input("Enter a slope value in degrees: ")
#print(f"The slope you entered is, {slope}, degrees")
#slopeFloat = float(slope)

# slope in radians
#slopeRadians = round(math.radians(slopeFloat),2)
#print(f"This corresponds to a slope of {slopeRadians}, in radians.")

# sl4
#slopeFraction = math.tan(slopeRadians)
#print(f"This corresponds to a slope of, {slopeFraction}, (m/m)")

#s slope factor
#S_factor = round((0.065 + (0.045 * slopeFloat) + (0.0065* slopeFloat ** 2)),3)
#print(f"the S_factor value is: {S_factor}")

