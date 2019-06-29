# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:49:20 2019

@author: MCA
"""
import numpy as np

A = np.array([[8, 3, -2], [-4, 7, 5], [3, 4, -12]])
b = np.array([9, 15, 35])
x = np.linalg.solve(A, b)
