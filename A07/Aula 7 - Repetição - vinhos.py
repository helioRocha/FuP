
teste = True

quantidadeTinto = 0
quantidadeBranco = 0
quantidadeRose = 0

while teste:
	print 'Digite o tipo de vinho:'
	print 'T - Tinto, B -  Branco, R - Rose'
	print 'e S para sair!'
	tipoVinho = raw_input()
	
	if tipoVinho == 'T':
		quantidadeTinto = quantidadeTinto + 1
	elif tipoVinho == 'B':
		quantidadeBranco = quantidadeBranco + 1
	elif tipoVinho == 'R':
		quantidadeRose = quantidadeRose + 1
	elif tipoVinho == 'S':
		teste = False
	else:
		print 'Opcao invalida!'


totalVinhos = quantidadeTinto + quantidadeBranco + quantidadeRose
print 'A porcentagem de Tinto:', quantidadeTinto/float(totalVinhos)*100, '%'
print 'A porcentagem de Branco:', quantidadeBranco/float(totalVinhos)*100, '%'
print 'A porcentagem de Rose:', quantidadeRose/float(totalVinhos)*100, '%'
