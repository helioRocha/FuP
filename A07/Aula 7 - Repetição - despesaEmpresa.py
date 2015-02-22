print 'Salario dos funcionarios da empresa'

x = 0
total = 0

while x < 3:
	print 'Funcionario', x + 1
	print 'Digite o nome do funcionario'	
	f = raw_input()
	print 'Digite o salario do funcionario'
	salario = input()
	total = salario + total
	x = x + 1
	
print 'A despesa da empresa e:', total
print 'A media de despesa e:', total/float(x)
