l1 = []
l2 = []
listaSoma = []
for i in range(10):
	print 'Digite o elemento da lista 1'
	l1.append(input())

for i in range(10):
	print 'Digite o elemento da lista 2'
	l2.append(input())

for i in range(10):
	listaSoma.append(l1[i] + l2[i])

for i in range(10):
	print listaSoma[i]

