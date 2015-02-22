print 'Digite o primeiro valor'
valor1 = input()

print 'Digite o segundo valor'
valor2 = input()

print 'Digite a operacao: \n1. Soma\n 2. Subtracao\n 3. Multiplicacao\n 4.Divisao'
operacao = raw_input()

if operacao == '+':
	print valor1 + valor2
elif operacao == '-':
	print valor1 - valor2
elif operacao == '*':
	print valor1*valor2
elif operacao == '/':
	print valor1/float(valor2)
else:
	print 'Operacao invalida!'
