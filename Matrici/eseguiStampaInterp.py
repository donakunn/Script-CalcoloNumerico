#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:29:15 2021

@author: kun
"""

import numpy as np
from printGrafInterp import printGraficoInterp

def f(x):
    y = np.exp(-x) * np.sin(2*x) 
    return y

def g(x):
    y = 1 / (1 + x**2)
    return y

def eseguiStampaInterp():
    printGraficoInterp(g,-5,5,80)
    return