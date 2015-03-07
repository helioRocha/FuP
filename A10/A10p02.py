media = []
qA = 3 # input('Quantidade de alunos da turma: ')
soma = 0

for i in range(qA):
	nota1 = (input('Nota1: '))
	nota2 = (input('Nota2: '))
	med = (nota1+nota2)/2.0
	soma += med	
	media.append(med)

M = float(soma)/qA
print M

c = 0
for k in range(qA):
	if media[k]>=M:
		c += 1

print c
#
