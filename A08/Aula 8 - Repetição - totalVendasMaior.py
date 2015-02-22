print 'Digite a quantidade de vendedores:'
quantidadeVendedores = input()

total = 0

for x in range(quantidadeVendedores):
	print 'Digite a quantidade de vendas do vendedor', x+1
	vendas = input()
	if x == 0:
		menor = vendas
		maior = vendas
		idVendedor = x + 1

	total = total + vendas
	
	if vendas > maior:
		maior = vendas
		idVendedor = x + 1

	if vendas < menor:
		menor = vendas
		
print 'O total de vendas foi:', total
print 'A media de vendas foi:', float(total)/quantidadeVendedores
print 'A maior quantidade de vendas foi:', maior
print 'O vendedor que mais vendeu foi:', idVendedor
print 'A menor quantidade de vendas foi:', menor
