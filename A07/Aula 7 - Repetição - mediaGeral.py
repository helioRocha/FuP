print 'Media Geral da Turma'
print 'Digite a quantidade de alunos'
quantidadeAlunos = input()

x = 0
soma = 0

while x < quantidadeAlunos:
	print 'Digite a nota 1 do aluno', x+1
	nota1 = input()
	print 'Digite a nota 2 do aluno', x+1
	nota2 = input()

	media = (nota1 + nota2)/2.0
	print 'A media do aluno', x+1, ':', media
	
	#Verificar a situacao

	soma = media + soma
	x = x + 1
	
print 'A media Geral:', soma/float(quantidadeAlunos)
