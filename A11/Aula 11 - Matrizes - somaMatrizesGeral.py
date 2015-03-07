print 'Digite a quantidade de linhas'
linhas = input()
print 'Digite a quantidade de colunas'
colunas = input()

matriz1 = []
matriz2 = []
matrizSoma = []
for i in range(linhas):
	matriz1.append([])
	matriz2.append([])
	matrizSoma.append([])

for i in range(linhas):
	for j in range(colunas):
		print 'Digite o elemento', i, j
		matriz1[i].append(input())

print matriz1 

for i in range(linhas):
	for j in range(colunas):
		print 'Digite o elemento', i, j
		matriz2[i].append(input())

print matriz2

for i in range(linhas):
	for j in range(colunas):
		soma = matriz1[i][j]+matriz2[i][j]
		matrizSoma[i].append(soma)

print matrizSoma
