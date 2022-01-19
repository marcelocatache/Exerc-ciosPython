#CÁLCULO DE ÁREA E QUANT. DE TINTA
larg = float(input('Largura de parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
vol = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
print('Você precisará de {}L de tinta.'.format(vol))
