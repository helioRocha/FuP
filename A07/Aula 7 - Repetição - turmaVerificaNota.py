continuar = True
while continuar:
	
	print 'Digite a nota 1'
	nota1 = input()
	while nota1 > 10 or nota1 < 0:
		print 'Nota Invalida!'
		print 'Digite a nota 1'
		nota1 = input()
	
	print 'Digite a nota 2'
	nota2 = input()
	while nota2 > 10 or nota2 < 0:
		print 'Nota Invalida!'
		print 'Digite a nota 2'
		nota2 = input()

	media = (nota1 + nota2)/2.0
	print 'A media e:', media

	if media >= 7:
		print 'Aprovado!'
	elif media >= 3:
		print 'Prova Final!'
	else:
		print 'Reprovado!'
	
	print 'Digite N para terminar'
	opcao = raw_input()
	if opcao == 'N':
		continuar = False

print 'Programa Terminado!'
