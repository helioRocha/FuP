print 'Digite a quantidade de termos'
termos = input() #4
qtd = termos/3 #1
resto = termos%3 #1

valor1 = 2
valor2 = 7
valor3 = 3

for i in range(qtd):
	print valor1
	print valor2
	print valor3
	valor1 = valor1*2
	valor2 = valor2*3
	valor3 = valor3*4

if resto == 1:
	print valor1
if resto == 2:
	print valor2
	print valor3
