print 'Digite um valor para verificar a paridade'
numero = input()

if numero >= 0:
	if numero%2==0:
		print numero, 'e par!'
	else:
		print numero, 'e impar!'
else:
	print 'Numero negativo!'

