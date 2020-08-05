# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 17:10:26 2016

@author: AzuMig
"""
import numpy as np
def bisection(f,a,b,tol=0.001):
    if f(a)*f(b)>0:
        print "El intervalo desde",a,"hasta",b,"es invalido"
        return None
    while (b-a)/2.0>tol:
        m=(a+b)/2.0
        print"Se está probando con el punto medio:",m
        if f(m)==0:
            break
        if f(a)*f(m)<0:
            b=m
        else:
            a=m
    print "La raiz es:",m
    return m

bisection(x^2+2,5,7,0.001)