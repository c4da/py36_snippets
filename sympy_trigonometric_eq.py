# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:59:21 2019

@author: MCA
"""
import numpy as np
from sympy import *
#import math

#x1 = Symbol('x1',real = True)
#x2 = Symbol('x2',real = True)
#x3 = Symbol('x3',real = True)

x1, x2, x3 = symbols('x1 x2 x3')

x = 0
y = 0
z = 0

e1= Eq(sin(x1)+cos(x3)+sin(x2)-x)
e2= Eq(cos(x2)+sin(x1)+sin(x3)-y)
e3= Eq(sin(x3)+cos(x1)+cos(x2)-z)

sol = solve([e1,e2,e3],x1,x2,x3)
