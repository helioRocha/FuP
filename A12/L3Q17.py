#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
17) Escreva um programa que receba uma lista de quantidade
de elementos digitada pela usuario e depois recebe um outro
valor. O programa deve mostrar na tela "ACHADO" se o valor
estiver na lista e "NAO ACHADO" caso contrario.'''

q = input('Quantidade de elementos da lista: ')
print

lst = []  # lista vazia
for i in range(q):
    print 'Inserir elemento', (i+1)
    lst.append(input('Elemento: '))  # preenchimento da lista vazia
    print
    
v = input('Informar um valor: ')
print

# # verifica se o elemento informado consta na lista (apenas uma resposta)
# #for i in range(q):
# if v in lst:
#     print 'ACHADO'
# else:
#     print 'NAO ACHADO'

#print lst

tam = len(lst)  # tamanho da lista
achei = 0  # contador para verificacao de sucesso na procura (acima de 0 indica sucesso)
for i in range(tam):
    if v == lst[i]: # se valor constar na lista:
        achei += 1 # valor achado

if achei > 0: print 'ACHADO'
else: print 'NAO ACHADO'
