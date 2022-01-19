#CÁLCULO DE CATETOS

# Faça um programa que leia o comprimento do cateto oposto 
# e do cateto adjacente de um triângulo retângulo, calcule 
# e mostre o comprimento da hipotenusa.

# |  .
# |      .
# |_         .
# |º|____________

# co = float(input('Cateto Oposto: '))
# ca = float(input('Cateto Adjacente: '))
# hi = ((co ** 2) + (ca ** 2))**0.5 # (1/2)
# print('O valor da Hipotenusa é {:.2f}'.format(hi))

import math
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
hi = math.hypot(co,ca)
print('O valor da Hipotenusa é {:.2f}'.format(hi))

from math import hypot
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
hi = hypot(co,ca)
print('O valor da Hipotenusa é {:.2f}'.format(hi))
