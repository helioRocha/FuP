print 'Digite a quantidade de funcionarios'
quantidade = input()
salarios = []
gerentes = []
#Colocar os elementos nas listas
for i in range(quantidade):
	print '(G)erente ou (N)ao?'
	opcao = raw_input()
	if opcao == 'G':
		gerentes.append(True)
	else:
		gerentes.append(False)
	print 'Digite o salario do funcionario'
	salarios.append(input())

#Somar os salarios
soma = 0
for i in range(quantidade):
	soma = soma + salarios[i]

print 'Gasto Atual da Empresa:', soma
media = float(soma)/quantidade
#Contar gerentes com salario maior que a media salarial
gerenteAcimaMedia = 0
for i in range(quantidade):
	if salarios[i]>media and gerentes[i] == True:
		gerenteAcimaMedia = gerenteAcimaMedia + 1

print 'Gerentes Acima Media Atual:', gerenteAcimaMedia

#Atualizar os salarios
for i in range(quantidade):
	if gerentes[i] == True:
		salarios[i] = salarios[i]*1.1
	else:
		salarios[i] = salarios[i]*1.05

#Somar os salarios
soma = 0
for i in range(quantidade):
	soma = soma + salarios[i]

print 'Novo Gasto:', soma

media = float(soma)/quantidade

#Contar gerentes com salario maior que a media salarial
gerenteAcimaMedia = 0
for i in range(quantidade):
	if salarios[i]>media and gerentes[i] == True:
		gerenteAcimaMedia = gerenteAcimaMedia + 1

print 'Gerentes Acima Media Nova:', gerenteAcimaMedia
