print 'Digite o salario do funcionario'
salario = input()

print 'Digite as vendas do funcionario'
vendas = input()

if vendas > 2000:
	salario = salario + salario*10/100.0
	print 'salario e:', salario
else:
	if vendas >= 1000:
		salario = salario + salario * 5 / 100.0
		print 'salario e:', salario
	else:
		print 'Nao teve aumento'
