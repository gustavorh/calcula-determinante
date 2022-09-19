# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 10:30:32 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de lSa universidad.

"""
import math

a = input('Ingrese un valor para a: ')
a = int(a)

b = input('Ingrese un valor para b: ')
b = int(b)

c = input('Ingrese un valor para c: ')
c = int(c)

determinante = (pow(b, 2) - 4 * a * c)
determinante = math.sqrt(determinante)

if determinante > 0:
    print(f'X1 = {(-b + determinante)//(2 * a)}')
    print(f'X2 = {(-b - determinante)//(2 * a)}')
elif determinante < 0:
    print('No existe solución real')
else:
    print(f'X = {-b / (2 * a)}')
