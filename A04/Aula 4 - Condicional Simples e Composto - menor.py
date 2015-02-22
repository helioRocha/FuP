print 'Digite o primeiro valor'
valor1 = input()

print 'Digite o segundo valor'
valor2 = input()

print 'Digite o terceiro valor'
valor3 = input()

if valor1 < valor2 and valor1 < valor3:
	print valor1, 'e o menor!'

if valor2 < valor1 and valor2 < valor3:
	print valor2, 'e o menor!'

if valor3 < valor2 and valor3 < valor1:
	print valor3, 'e o menor!'
