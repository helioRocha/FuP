print 'Digite o valor de n'
n = input()

soma = 0

expressao = ''

for i in range(2, n+1):
	soma = soma + 1.0/i
	if i < n:
		expressao = expressao + '(1.0/' + str(i) + ')+'
	else:
		expressao = expressao + '(1.0/' + str(i) + ')'

print 'o valor da expressao:', expressao
print 'deu:', soma
