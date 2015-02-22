print 'Digite o salario'
salario = input()
print 'Digite o valor da primeira conta'
conta1 = input()
print 'Digite o valor da segunda conta'
conta2 = input()

multa1 = conta1*2/100.0
multa2 = conta2*2/100.0

conta1 = conta1 + multa1
conta2 = conta2 + multa2

restante = salario - (conta1 + conta2)

print 'A multa da conta 1 e:', multa1
print 'A multa da conta 2 e:', multa2
print 'O salario restante e:', restante
