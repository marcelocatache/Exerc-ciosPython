##########################
# OPERADORES ARITMÉTICOS #
#                        #
# Regras de Procedência  #
# de equação:            #
#  1 :   ()              #
#  2 :   **              #
#  3 :   *  /  //  %     #
#  4 :   +  -            #
##########################

#a=3
#b=5
#c=4
#d=2
#e=a*b+c**d
#e=a*(b+c)**d
#print(e)

#print('Oi'*4) #Resultado: OiOiOiOi

#SOMA DE VALORES DE VARIÁVEIS
n1=int(input('Um valor: '))
n2=int(input('Outro valor: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma é {},\n o produto é {},\n a divisão é {:.3f}'.format(s, m, d), end=',\n ')
print('a divisão inteira é {}\n e a potência é {}'.format(di, e))
