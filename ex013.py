#CÁLCULO DE AUMENTO DE SALÁRIO DE 15%
sal = float(input('Qual é o salário? R$'))
aum = sal + (sal * 15 / 100) #(sal / 100) * 115
print('O salário com aumento de 15% é: R${:.2f}'.format(aum))
