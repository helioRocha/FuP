'''
Faça um programa que recebe do usuário os 
elemento de um lista com 10 elementos e 
ordena a lista em ordem crescente.'''

qE = input('Quantidade de elementos: ')
lst = []
for i in range(qE):
    lst.append(input('Inserir elemento: '))


    
print sorted(lst, reverse = False)
lst.sort(reverse = False)

'''
Modifique o programa anterior para ordernar 
um lista com qualquer quantidade de 
elementos.'''
