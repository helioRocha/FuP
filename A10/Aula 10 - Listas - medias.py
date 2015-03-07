print 'Digite a quantidade de alunos'
quantidade = input()

medias = []
soma = 0
for i in range(quantidade):
	print 'Digite a primeira nota'
	nota1 = input()

	print 'Digite a segunda nota'
	nota2 = input()

	medias.append((nota1 + nota2)/2.0)
	soma = soma + medias[i]

mediaTotal = float(soma)/quantidade

acimaMedia = 0
for i in range(quantidade):
	if medias[i] >= mediaTotal:
		acimaMedia = acimaMedia + 1

print 'A quantidade de alunos com media acima ou igual a', mediaTotal, ':', acimaMedia
