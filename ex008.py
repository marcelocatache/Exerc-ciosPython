# UNIDADES DE MEDIDA

# quilometros
## hectometros
### decametros
#### decimetros
##### centimetros
###### milimetros

m=float(input('Digite a medida: '))
km=m*0.001
hm=m*0.01
dam=m*0.1
dm=m*10
cm=m*100
mm=m*1000
print('A medida de {}m corresponde a:'.format(m))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{:.1f}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))
