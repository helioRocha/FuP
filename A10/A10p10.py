'''
Uma empresa quer que você faça um 
programa para controlar e atualizar o salário 
dos funcionários. Um funcionário que não é 
gerente terá um aumento de 5%, um 
funcionário que é gerente ganha 10% de 
aumento. Seu programa deve atualizar os 
salários, mostrar o gasto atual e o novo gasto 
da empresa com o salário dos funcionários. 
Além disso, seu programa deve mostrar 
quantos gerentes ganhavam e quantos vão 
ganhar mais do que a média salarial da 
empresa.'''

qtde = input('Quantidade de funcionarios: ')
#minG = input('Salario-minimo gerente: ')

salVelho, salVelhoG = [], [] # Lista: Salario anterior de funcionarios (salVelho) e gerentes (salVelhoG)
salNovo, salNovoG = [], [] # Lista: Salario posterior de funcionarios (salNovo) e gerentes (salNovoG)
c1 = 0 # contador para soma dos salarios antigos
for i in range(qtde):
	print 'Se o funcionario for gerente entao tecle 1, caso contrario tecle ENTER.'
	gerente = raw_input()
	print 'Informar o salario do funcionario: '
	sVelho = input()
	c1 += sVelho
	if gerente == '1':
		salVelhoG.append(sVelho)
		salNovoG.append(sVelho * 1.10)
	else:
		salVelho.append(sVelho)
		salNovo.append(sVelho * 1.05)
	
sV = salVelho + salVelhoG # Listas dos salarios anteriores de funcionarios e gerentes concatendas
sN = salNovo + salNovoG # Listas dos salarios posteriores de funcionarios e gerentes concatendas

msA = float(c1/qtde) # Media salarial anterior (funcionarios e gerentes)
c1a = 0 # contador para gerentes com salario maior do que a media (periodo anterior ao aumento)
for i2 in range(len(salVelhoG)):
	if salVelhoG[i2]>msA:
		c1a += 1

c2 = 0 # contador para soma dos salarios novos
for j in range(len(sN)):
	c2 += sN[j]

msP = float(c2/qtde) # Media salarial posterior (funcionarios e gerentes)
c2a = 0 # contador para verificar gerentes com salario maior do que a media (periodo posterior ao aumento)
for i3 in range(len(salVelhoG)):
	if salVelhoG[i3]>msA:
		c2a += 1
	
#print sV
#print sN
print 'Gasto anterior, em R$:', c1
print 'Media salarial anterior', msA
print 'Quantidade de gerentes que ganhavam mais do que a media salarial (anterior) da empresa:', c1a
print 'Gasto posterior, em R$:', c2
print 'Media salarial posterior', msP
print 'Quantidade de gerentes que vao ganhar mais do que a media salarial (posterior) da empresa:', c2a

