'''
Fazer um programa que recebe as duas notas 
de cada aluno de uma turma. O programa deve 
mostrar a média geral da turma e a quantidade 
de alunos com média maior ou igual a média 
da turma.'''
n1 = []
n2 = []
med= []
m = 0
#n = input('numeros de alunos na turma: ')
for i in range(input('numeros de alunos na turma: ')):
    n1.append(float(input('Nota 1: ')))
    n2.append(float(input('Nota 2: ')))
    med.append((n1[i] + n2[i])/2.)

mGlobal = round(sum(med)/len(med), 2)

p = 0
for i in range(len(med)):
    if med[i] >= mGlobal:
        p += 1

print p
