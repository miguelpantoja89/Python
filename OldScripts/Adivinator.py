# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo 2016
"""
from random import randint
r=randint(1,1000)
score=0
print ("Haga su intento")
print ("Un número entre uno y mil")
while True:
    score= score+1
    intento= input()
    intento=float(intento)
    if intento<r:
        print ("El número es mayor")
    elif intento>r:
        print ("El número es menor")
    elif intento==r:
        if score<7:
            print("Eres un maquina")
        print("Lo lograste en:",score)
        break

    
    
   
        
