#CÁLCULO DE PREÇO COM DESCONTO DE 5%

#preco = float(input('Qual é o peco do produto? R$'))
#desc = preco * 0.95
#print('O preço do produto com desconto é R${:.2f}'.format(desc))

preco = float(input('Qual é o peco do produto? R$'))
desc = preco * 5 / 100
novo = preco - (preco * 5 / 100) #desc = preco * 95 / 100
print('O valor do desconto é de R${:.2f}'.format(desc))
print('O preço do produto com desconto é R${:.2f}'.format(novo))
