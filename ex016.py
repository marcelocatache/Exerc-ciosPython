#EXIBIÇÃO DE PARTE INTEIRA DE NÚMERO REAL

# Crie um programa que leia um número Real qualquer pelo 
# teclado e mostre na porção (parte) inteira.
# Exemplo: 
# Digite um número: 6.127
# O número 6.127 tem parte inteira 6.

# from math import floor
# num = float(input('Digite um número real: '))
# print('O valor {} tem como parte inteira {} '.format(num, floor(num)))

import math
num = float(input('Digite um número real: '))
print('O valor {} tem como parte inteira {} '.format(num, math.trunc(num)))

from math import trunc
num = float(input('Digite um número real: '))
print('O valor {} tem como parte inteira {} '.format(num, trunc(num)))

num = float(input('Digite um número real: '))
print('O valor {} tem como parte inteira {} '.format(num, int(num)))
