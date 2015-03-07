matriz = [[],[],[]]
for i in range(3):
	for j in range(2):
		print 'Digite o elemento', i, j
		matriz[i].append(input())

print matriz
print 'Digite um valor real escalar para multiplicar com a matriz'
escalar = input()

matrizResultado = [[],[],[]]
for i in range(3):
	for j in range(2):
		multiplicacao = escalar*matriz[i][j]
		matrizResultado[i].append(multiplicacao)

print matrizResultado
