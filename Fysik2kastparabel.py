#Programmeringsuppgift 1 i Fysik 2
from math import *
import math
 
V = int(input("Ange hastighet: "))
Theta = int(input("Ange vinkel: "))
Theta = math.radians(Theta)
S = sin
C = cos
R = radians
DeltaT = 0.001
g = 9.82
V2 = V**2
 
KPL = ((V2)/g)*(math.sin(Theta)+((math.cos(Theta))**2) * math.log((math.sin(Theta)+1)/(math.cos(Theta)))) # bågens längd,exakt värde. Algebraisk metod.
def Ode(V,Theta):
   
    startvX = V* C(Theta)
    startvY = V * S(Theta)
    X = startvX * DeltaT
    x = 0.0
    y = 0.0001
    t = 0.0
    KPL2 = 0
 
    while (y>0):
        Y = DeltaT * (startvY - g *t)
        KPL2 += math.sqrt((X**2)+(Y**2)) # Längd på parabeln med numerisk metod, pythagoras. Är beroende av DeltaT, inte lika exakt som den algebraiska metoden.
        y = y + DeltaT * (startvY - g *t)
        t = t + DeltaT
         
    x = startvX * t
    return print("Objektet kom", x, "meter.", "bågens längd är: ", KPL ,"meter (algebraiskt) och ", KPL2,"(numeriskt)." )
 
   
 
print(Ode(V,Theta))
 
 
 
