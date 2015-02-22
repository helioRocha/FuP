
x = True

soma = 0
qtdPares = 0

while x:
	print 'Digite um valor natural ou negativo para encerrar'
	valor = input()
	if valor < 0:
		x = False
	elif valor%2 == 0:
		soma = soma + valor
		qtdPares = qtdPares + 1

print 'A media dos pares:', float(soma)/qtdPares
