'''
Fa�a um programa que recebe do usu�rio os 
elementos de duas listas com 10 elementos 
cada. O seu programa deve somar as duas 
listas e mostrar a lista resultante. A soma de 
listas � a soma das posi��es correspondentes'''

l1 = []
l2 = []
l3 = []
for i in range(10):
    l1.append(input('elemento da lista 1: '))
    l2.append(input('elemento da lista 2: '))
    l3.append(l1[i]+l2[i])
    
l4 = [l1[i] + l2[i] for i in range(len(l1))]