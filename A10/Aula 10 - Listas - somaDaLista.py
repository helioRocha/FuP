lista = []
for i in range(10):
	print 'Digite o elemento da lista'
	lista.append(input())
	
soma = 0
for i in range(10):
	soma = soma + lista[i]

print 'A soma da lista e:', soma
