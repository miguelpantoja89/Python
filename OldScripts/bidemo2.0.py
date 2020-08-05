# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 17:37:41 2016

@author: AzuMig
"""
import matplotlib.pyplot as plt
import numpy as np
from bisection2 import bisection

def biplot(f,a,b,nom,color,l):
    r=bisection(f,a,b)
    x=np.linspace(a,b)
    y=f(x)
    plt.figure('Represntacion grafica',figsize=(10,6))
    plt.plot(x,y,label=nom,color=color,linewidth=l)
    plt.xlabel('abscisas')
    plt.ylabel('ordenadas')
    plt.title('Bidemo')
    plt.text(0,-40, r'$red points=root$')
    plt.scatter(r,0,edgecolors='r',linewidth=4)
    plt.legend(loc='right')
    plt.grid(True)
    plt.hold(True)
    return
    
biplot(lambda x: np.sin(x+23),-5,5,'$sin(x+23)$','g',1)
biplot(lambda x: np.cos(x),-5,5,'$cosx$','b',1.1)
biplot(lambda x: x**3+2,-5,5,"$x^3+2$", 'y' ,1)
biplot(lambda x: np.log(x),-5,5,'$logx$','pink',1)
biplot(lambda x: x**2+5*x+2,-5,5,'$x^2+5x+2$','orange',0.9)
biplot(lambda x: x**2+6*x+4,-5,5,'$x^2+6x+4$','purple',0.9)
biplot(lambda x: x+2,-5,5,'$x+2$','lime',1)
biplot(lambda x: np.sin(x+2)/2.0,-5,5,'$sinx+2/2$','k',0.9)
biplot(lambda x: np.cos(x+3)/2.0,-5,5,'$cosx+3/2$','c',1)
biplot(lambda x: (np.sin(x))*2,-5,5,'$sin^2x$','m',1.1)
biplot(lambda x: np.cos(x),-5,5,'$cosx$','gold',1.1)
biplot(lambda x: -x**2,-5,5,"$-x^2$", 'aqua',1.1)
biplot(lambda x: np.log(x),-5,5,'$logx$','mediumblue',0.9)
biplot(lambda x: np.sqrt(x),-5,5,'$sqrtx$','orchid',1)
biplot(lambda x: x**3,-5,5,'$x^3$','plum',1)
biplot(lambda x: x**2,-5,5,'$x^2$','fuchsia',1)
biplot(lambda x: np.tan(x),-5,5,'$tgx$','yellowgreen',1)
biplot(lambda x: np.exp(x),-5,5,'$e^x$','indigo',1)
biplot(lambda x: -x**2+6*x+4,-5,5,'$-x^2+6x+4$','salmon',1)
biplot(lambda x: -x**2-2,-5,5,'$x^2+10x+2$','darkred',1)
plt.show()






