print 'Digite a quantidade de vendedores'
qtdVendedores = input()

soma = 0

for x in range(qtdVendedores):
	print 'Digite as vendas do vendedor', x+1
	vendas = input()
	soma = soma + vendas

print 'O total de vendas foi:', soma
print 'A media de vendas foi:', float(soma)/qtdVendedores
