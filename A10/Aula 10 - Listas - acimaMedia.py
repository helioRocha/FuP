print 'Digite a quantidade de alunos da turma'
quantidade = input()

#Criar uma lista com as medias
medias = []
for i in range(quantidade):
	print 'Digite a nota 1'
	nota1 = input()
	print 'Digite a nota 2'
	nota2 = input()
	medias.append((nota1 + nota2)/2.0)
	
#Soma as medias
soma = 0
for i in range(quantidade):
	soma = soma + medias[i]

#media Total
mediaTotal = float(soma)/quantidade

#Conta a quantidade de alunos com media maior ou igual
acimaMedia = 0
for i in range(quantidade):
	if medias[i] >= mediaTotal:
		acimaMedia = acimaMedia + 1

print 'A quantidade de alunos com media maior ou igual a', mediaTotal, 'foi:', acimaMedia
