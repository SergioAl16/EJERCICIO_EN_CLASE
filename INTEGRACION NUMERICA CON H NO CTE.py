# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin - 161259
03/10/2023

INTEGRACION NUMERICA CON H NO CONSTANTE
"""
import numpy as np
from scipy.interpolate import CubicSpline

x = [1,2,3.25,4.5,6,7,8,9,9.5,10]
y = [5,6,5.5,7,8.5,8,6,7,7,5]

IntTrap_sinh = 0

for i in range(1,len(y)):
    # Trapecio
    IntTrap_sinh += (y[i-1]+y[i])/2*(x[i]-x[i-1])

# Crear un objeto CubicSpline
cubic_spline = CubicSpline(x, y)

# Definir los límites de integración (a y b)
a = 1  # Límite inferior
b = 10  # Límite superior

# Calcular la integral utilizando CubicSpline.integrate
integral = cubic_spline.integrate(a, b)

# Imprimir el resultado
print("Integral de {} a {}: {}".format(a, b, integral))
print(IntTrap_sinh)

# EJERCICIO EN CLASE 2
# x = [1,2,3.25,4.5,6,7,8,9,9.5,10]
# y = [5,6,5.5,7,8.5,8,6,7,7,5]

# Definir los límites de integración (a y b)
# a = 1  # Límite inferior
# b = 10  # Límite superior
