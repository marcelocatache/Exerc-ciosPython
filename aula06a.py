#######################################
#         TIPOS PRIMITIVOS:           #
#                                     #
#   int:  7 / -4 / 0 / 9875           #
# float:  4.5 / 0.076 / -15.223 / 7.0 #
#  bool:  True / False                #
#   str:  'Olá' / '7.5' / ''          #
#######################################

#CONCATENAÇÃO (sem soma)
#num1=input('Digite um valor: ')
#print(type(num1))

#SOMA DE INTEIROS
n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s=n1+n2
#print('A soma entre',n1,'e',n2,'vale',s)
print('A soma entre {} e {} vale {}'.format(n1,n2,s))
#print(type(n1))
#print(type(n2))


#EXEMPLO DE FLOAT
print('==============================')
f=float(input('Digite um valor FLOAT: '))
print(f)
print(type(f))


#EXEMPLO DE BOOLEAN0s(bool)
print('==============================')
b=bool(input('Digite um valor BOOL: '))
print(b) #ele vai analisar se você digitou algum valor
print(type(b))


#EXEMPLO DE STR
print('==============================')
s=str(input('Digite um valor STR: ')) #s=input('Digite um valor STR: ')
print(s)
print(type(s))
#se eu não declarar o tipo de variável, ele será string


#ALGUNS MÉTODOS DE TESTES DE TIPOS


#MÉTODO PARA VERIFICAR SE VARIÁVEL É NÚMERICA
print('==============================')
num2=input('Digite algo: ')
print(num2.isnumeric())
#print(type(num2))


#MÉTODO PARA VERIFICAR SE VARIÁVEL É ALFABÉTICO
print('==============================')
num3=input('Digite algo: ')
print(num3.isalpha())
#print(type(num3))


#MÉTODO PARA VERIFICAR SE VARIÁVEL É ALFA-NUMÉRICO
print('==============================')
num4=input('Digite algo: ')
print(num4.isalnum())
#print(type(num4))
