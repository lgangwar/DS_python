# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 00:54:45 2018

@author: Lalit
"""

from math import *
def polysum(n,s):
    '''
    input: number of input two, 
            n = number of sides
            s = length of side
    polygon Info:
            area of polygon = 0.25*n*s^2 / tan(pi/n)
            perimeter of polygon = s+s+s+........n times = n * s
            because regular polygon has all sides equal to each other
    
    output: sum of polygon's area and square of its perimeter
            round upto 4 decimal places
    '''
	
	i = 12
    areaPolygon = (0.25*n*(s**2))/(tan(pi/n))
    perimeterPolygon = n * s
    ans = areaPolygon + perimeterPolygon**2
    return round(ans,4)
