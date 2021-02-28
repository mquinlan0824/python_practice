# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 18:23:03 2020

@author: Asus
"""

import math

"""
Solving Manning equation which describes the flow
of water through a channel.

input = r: hydraulic radius in meters; s: sfc roughness and slope (unitless);
n: Manning coefficient of roughness [0.01 = smooth; 0.08 = rough]
output = v: velocity (m/sec)
"""

hydraulic_radius = 3.0 # units = meters
slope = 0.1 # unitless
Manning_coefficient = 0.01 # unitless

water_velocity = round(((hydraulic_radius**(2.0/3.0)) * (slope**(1.0/2.0)) / \
Manning_coefficient), 2)
print(f"With a hydraulic radius of {hydraulic_radius} m, the flow speed is \
{water_velocity} m/sec.")
