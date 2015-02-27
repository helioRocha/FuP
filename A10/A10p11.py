'''
Faça um programa que recebe do usuário os 
elemento de um lista com 10 elementos e 
ordena a lista em ordem crescente.'''

'''qE = input('Quantidade de elementos: ')
lst = []
for i in range(qE):
    lst.append(input('Inserir elemento: '))
    
print sorted(lst, reverse = False)
#lst.sort(reverse = False)'''

lst = []
for i in range(10):
	lst.append(input('Inserir elemento: '))
	
for j in range(10):
    for k in range(j,10):
        if lst[j] > lst[k]:
            aux = lst[j]
            lst[j] = lst[k]
            lst[k] = aux

'''
Modifique o programa anterior para ordernar 
um lista com qualquer quantidade de 
elementos.'''
