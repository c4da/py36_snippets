# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:25:03 2019

@author: MCA
"""

import numpy as np
import math 

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


def find_nearest_sorted(array,value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return array[idx-1]
    else:
        return array[idx]