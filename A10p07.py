'''
Fa�a um programa recebe os elementos de 
uma lista com 10 posi��es. Seu programa deve 
mostrar a soma dos elementos dessa lista.'''

lst = []
c = 0
for i in range(10):
    lst.append(input('Digite um inteiro: '))
    c += lst[i]

print c
print sum(lst)