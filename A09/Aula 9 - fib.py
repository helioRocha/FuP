print 'Digite a quantidade de termos da sequencia'
quantidade = input()

valor1 = 0
valor2 = 1

print valor1
print valor2

for i in range(3, quantidade+1):
	aux = valor1 + valor2
	valor1 = valor2
	valor2 = aux
	print valor2
	
