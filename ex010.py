#COTAÇÃO DE REAL PARA DÓLAR

#real = float(input('Quanto dinheiro você tem na carteira? R$'))
#print('Com {:.2f} você pode comprar US${:.2f}'.format(real, real/5.64)) #3.27 

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.64 #(09/01/2022)
print('Com {:.2f} você pode comprar US${:.2f}'.format(real, dolar))
