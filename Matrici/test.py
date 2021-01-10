#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 18:36:13 2021

@author: kun
"""
from pylab import *

def test():
    x=linspace(0,2*pi,100)
    y=sin(x)*exp(-x)
    y1=sin(3*x)*exp(-x)
    y2=sin(5*x)*exp(-x)
    plot(x,y,label="y=sin(x)*exp(x)")
    plot(x,y1,label="y=sin(3*x)*exp(-x)")
    plot(x,y2,label="y=sin(5*x)*exp(-x)")
    legend(loc='upper right')
    xlabel("asse x")
    ylabel("asse y")
    title("Grafico di tre funzioni") 
    return

test()