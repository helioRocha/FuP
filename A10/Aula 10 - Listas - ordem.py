lista = []

for i in range(5):
	lista.append(input())

for j in range(5):
	for i in range(j, 5):
		if lista[i] < lista[j]:
			aux = lista[j]
			lista[j] = lista[i]
			lista[i] = aux

print lista
