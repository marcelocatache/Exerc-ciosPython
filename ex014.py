#CONVERSOR DE TEMPERATURA DE ºC PARA ºF e K

cel = float(input('Qual a temperatura em graus Celsius (ºC): '))
fah = 9 * cel / 5 + 32  #cel * 1.8 + 32
kel = cel + 273.15
print('Essa temperatura em graus Fahrenheit (ºF) é: {:.1f} '.format(fah))
print('Essa temperatura em Kelvin (K) é: {:.2f} '.format(kel))
