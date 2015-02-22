l1 = []
l2 = []
soma = []
for i in range(3):
	print 'Digite o elemento', i, 'da lista 1'
	l1.append(input())

print l1
for i in range(3):
	print 'Digite o elemento', i, 'da lista 2'
	l2.append(input())
	l1[i] = l1[i] + l2[i]
	

print l2
print l1
