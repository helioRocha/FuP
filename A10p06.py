'''
Fa�a um programa que constr�i uma lista 
colocando o valor 0 nas posi��es pares e 1 nas 
posi��es �mpares'''

n = input('quantidade de elementos da lista: ')
lst = []
for i in range(n):
    if i%2==0:
        lst.append(0)
    else:
        lst.append(1)
        
print lst