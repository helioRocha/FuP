'''
Faça um programa que recebe do usuário os 
elemento de um lista com 10 elementos e 
ordena a lista em ordem crescente.'''

lst = []
for i in range(3):
    lst.append(input('Inserir elemento: '))


    
print sorted(lst, reverse = False)
lst.sort(reverse = False)

'''
Modifique o programa anterior para ordernar 
um lista com qualquer quantidade de 
elementos.'''