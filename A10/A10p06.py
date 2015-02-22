'''
Faça um programa que constrói uma lista 
colocando o valor 0 nas posições pares e 1 nas 
posições ímpares'''

n = input('quantidade de elementos da lista: ')
lst = []
for i in range(n):
    if i%2==0:
        lst.append(0)
    else:
        lst.append(1)
        
print lst
