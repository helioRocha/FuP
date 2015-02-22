print 'Digite a quantidade de funcionarios'

quantidadeFunc = input()

x = 0

soma = 0

while x < quantidadeFunc:
	print 'Digite o salario do funcionario', x+1
	salario = input()

	soma = soma + salario

	x = x + 1
	
print 'A despesa da empresa:', soma
print 'A media salarial e:', float(soma)/quantidadeFunc
