print 'Digite a quantidade de vendedores'
qtdVendedores = input()

soma = 0

for x in range(qtdVendedores):
	print 'Digite as vendas do vendedor', x+1
	vendas = input()
	
	if x == 0:
		menor = vendas
		maior = vendas
		vendedorMaior = x + 1
		vendedorMenor = x + 1
	
	if vendas > maior:
		maior = vendas
		vendedorMaior = x + 1

	if vendas < menor:
		menor = vendas
		vendedorMenor = x + 1

	soma = soma + vendas

print 'O total de vendas foi:', soma
print 'A media de vendas foi:', float(soma)/qtdVendedores
print 'A maior venda foi:', maior
print 'O vendedor com maior venda foi:', vendedorMaior
print 'A menor venda foi:', menor
print 'O vendedor com menor venda foi:', vendedorMenor

