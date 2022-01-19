# 
# Escreva um programa que pergunte a quantidade de Km 
# percorrido por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule a preço a pagar, sabendo que
# o carro custa R$60 por dia e R$ 0.15 por Km rodado.

#dias1 = int(input('Quantos dias alugados? '))
#km1 = float(input('Quantos Km rodados? '))
#diap1 = dias1 * 60
#kmp1 = km1 * 0.15
#pago1 = kmp1 + diap1
#print('O total a pagar é de R${:.2f} '.format(pago1))

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f} '.format(pago))
