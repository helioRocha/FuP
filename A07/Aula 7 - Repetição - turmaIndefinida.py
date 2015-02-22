continuar = True
i = 1
while continuar:
	print 'Digite a nota 1 do aluno', i, ':'
	nota1 = input()

	print 'Digite a nota 2 do aluno', i, ':'
	nota2 = input()

	media = (nota1+nota2)/2.0

	print 'A media do aluno e:', media

	if media >= 7:
		print 'Aprovado!'
	elif media >= 3:
		print 'Prova Final!'
	else:
		print 'Reprovado!'
	
	print 'Deseja continuar?'
	opcao = raw_input()
	if opcao == 'N':
		continuar = False
