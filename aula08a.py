#IMPORTAÇÃO DE MÓDULOS
# https://www.youtube.com/watch?v=oOUyhGNib2Q&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=24
# exemplo: import bebida
# exemplo: from doce import pudim


#Importação por Padrão: 
# onde ver quais são as bibliotecas que pode-se importar: 
# https://docs.python.org/3/library/numeric.html
# (versão Python 3.10.1)(acesso: 10/01/2022)
# (sempre verificar a versão do seu Python)

#Importação de Pacotes Extras:
# PyPI - the Python Package Index (Indice de Pacotes Extras)
# pypi.python.org
# https://pypi.org/

# biblioteca emoji do pypi
# import emoji
# print(emoji.emojize("Olá, Mundo :sunglasses:", use_aliases=True))
# # print(emoji.emojize("Olá, Mundo :earth_americas:", use_aliases=True))


# import [ctrl] + [space] (ver todas as bibliotecas)


#funções biblioteca math:
# ceil = arredonda pra cima
# floor = arredonda pra baixo
# trunc = elimina o número da vírgula pra frente (truncar)
# pow = potência (funciona de forma semelhante dos **)
# sqrt = raiz quadrada 
# factorial = cálculo fatorial de um número

# import math
# from math import sqrt
# from math import sqrt, ceil

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
#print('A raiz de {} é igual a {} '.format(num, raiz))
#print('A raiz de {} é igual a {} '.format(num, math.ceil(raiz)))
#print('A raiz de {} é igual a {} '.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {:.2f} '.format(num, raiz))
print('='*30)

from math import sqrt
#from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {} '.format(num, raiz))
#print('A raiz de {} é igual a {} '.format(num, floor(raiz)))
print('='*30)


#Classe random

import random
num = random.random()
# o método random (random.RANDOM) da classe random (RANDOM.random)
# importa um nº aleatório entre 0 e 1
print(num)
print('='*30)

import random
num = random.randint(1, 10)
print(num)
#randoniza um número inteiro entre 1 e 10
print('='*30)

