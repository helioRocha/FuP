matriz1 = [[],[],[]]
for i in range(3):
	for j in range(2):
		print 'Digite o elemento', i, j
		matriz1[i].append(input())

print matriz1

matriz2 = [[],[],[]]
for i in range(3):
	for j in range(2):
		print 'Digite o elemento', i, j
		matriz2[i].append(input())

print matriz2

matrizSoma = [[],[],[]]
for i in range(3):
	for j in range(2):
		soma = matriz1[i][j]+matriz2[i][j]
		matrizSoma[i].append(soma)

print matrizSoma
