print 'Digite a primeira nota'
nota1 = input()

print 'Digite a segunda nota'
nota2 = input()

media = (nota1+nota2)/2.0

print 'A sua media e: ', media

if media >= 7:
	print 'Aprovado Direto! Parabens!'

else:
	if media >= 3:
		print 'Prova Final! Boa Sorte!'
	else:
		print 'Reprovado! Tchau!'
