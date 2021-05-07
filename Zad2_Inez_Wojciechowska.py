# -*- coding: utf-8 -*-
"""
Created on Fri May  7 18:30:37 2021

@author: Inez
"""

def srednia(a,y):
    if a>0 and y>a:
        suma_niepodzielnych=0
        suma=0;
        for i in range(a,y+1):
            if i%2:
                suma_niepodzielnych+=1
                suma=suma+i
        print("Średnia arytmetyczna liczb nieparzystych z podanego przedziału:",a,y,"wynosi:",suma/suma_niepodzielnych)
    else:
        print("Podany przedział jest nieprawidłowy!")
            
    
   
    
   
    
a=input("Początek przedziału:")
y=input("Koniec przedziału:")


srednia(int(a),int(y))
    