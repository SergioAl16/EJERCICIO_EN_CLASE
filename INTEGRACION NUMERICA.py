# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin - 161259
03/10/2023

INTEGRACION NUMERICA
"""
import numpy as np

h = 0.0001
x = np.arange(0,np.pi*2,h)
y = np.exp(np.cos(x))

sumaTrapecio = y[0]+y[len(y)-1]
sumaSimpson13 = y[0]+y[len(y)-1] # Suma Simpson Un Tercio
sumaSimpson38 = y[0]+y[len(y)-1] # Suma Simpson Tres Octavos

for i in range(1,len(y)-1):
    # Trapecio
    sumaTrapecio += 2*y[i]
    
    # Simpson13
    if i%2 == 0: # todos los pares 
        sumaSimpson13 += 2*y[i]
    else:
        sumaSimpson13 += 4*y[i]
        
    # Simpson38
    if i%3 == 0:
        sumaSimpson38 += 2*y[i]
    else:
        sumaSimpson38 += 3*y[i]

# Cuando queires encontrar la h.................
# h = (y[i-1]+y[i])/2 * (x[i]-x[i-1])

# Calcula el volumen bajo la curva (integral)
VolumenTrapecio = np.pi * 2 * h / 2 * sumaTrapecio
VolumenSimpson13 = np.pi * 2 * h / 3 * sumaSimpson13
VolumenSimpson38 = np.pi * 2 * 3 * h / 8 * sumaSimpson38

print("Volumen (Trapecio):", VolumenTrapecio)
print("Volumen (Simpson13):", VolumenSimpson13)
print("Volumen (Simpson38):", VolumenSimpson38)

# Area bajo la curva
# IntTrapecio = h/2*sumaTrapecio
# IntSimpson13 = h/3*sumaSimpson13
# IntSimpson38 = 3*h/8*sumaSimpson38

# rint(IntTrapecio)
# print(IntSimpson13)
# print(IntSimpson38)

# EJERCICIO EN CLASE
# h = 0.0001
# x = np.arange(0,1,h)
# y = np.exp(x**2)

# EJERCICIO EN CLASE 2 

# PROBLEMA 1
# h = 0.0001
# x = np.arange(0,1,h)
# y = np.exp(x**2)

# PROBLEMA 2
# h = 0.1
# x = np.arange(0,3,h)
# y = x**2 * np.exp(x)

# PROBLEMA 3
# Calcula el volumen bajo la curva (integral)
# h = 0.0001
# x = np.arange(0,np.pi*2,h)
# y = np.exp(np.cos(x))

# VolumenTrapecio = np.pi * 2 * h / 2 * sumaTrapecio
# VolumenSimpson13 = np.pi * 2 * h / 3 * sumaSimpson13
# VolumenSimpson38 = np.pi * 2 * 3 * h / 8 * sumaSimpson38

# print("Volumen (Trapecio):", VolumenTrapecio)
# print("Volumen (Simpson13):", VolumenSimpson13)
# print("Volumen (Simpson38):", VolumenSimpson38)
