import numpy as np
import matplotlib.pyplot as plt

x=[]
y=[]

def fun_lin(a, b):

    il_dane = int(input("Jak długa ma być lista danych? "))
    miejsce= int(input("Od jakiej wartości x chcesz zacząć? "))
    kon = int(il_dane/2)
    for i in range(miejsce, kon):
        global x
        global y
        x.append(i)
        y.append(a*i + b)
    return x, y 



def fun_kw(a, b, c):
    
    il_dane = int(input("Jak długa ma być lista danych? "))
    miejsce= int(input("Od jakiej wartości x chcesz zacząć? "))
    kon = int(il_dane/2)
    
    for i in range(miejsce, kon):
        global x
        global y
        d = b*b - 4*a*c
        p = -b/(2*a)
        q = -d/(4*a)
        x.append(i)
        y.append(a*(i-p)**2 + q)
        
    return x, y

def fun_wyk(a, n):
    
    il_dane = int(input("Jak długa ma być lista danych? "))
    miejsce= int(input("Od jakiej wartości x chcesz zacząć? "))
    kon = int(il_dane/2)
    for i in range(miejsce, kon):
#        if (i != 0):  
#               nie wiem jak rowiązać dzielenie przez 0          
            global x
            global y
            x.append(i)
            y.append(a/(i**n))
            return x,y
        else:
            return x,y
    
    