print 'Digite o primeiro valor'
valor1 = input()

print 'Digite o segundo valor'
valor2 = input()

print 'Digite o terceiro valor'
valor3 = input()

if valor1 > valor2:
	aux = valor1
	valor1 = valor2
	valor2 = aux

if valor1 > valor3:
	aux = valor1
	valor1 = valor3
	valor3 = aux

if valor2 > valor3:
	aux = valor2
	valor2 = valor3
	valor3 = aux

print valor1, valor2, valor3
