#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
4) Crie um programa que receba uma lista de inteiros de 30
posicoes e depois cria uma segunda lista cujas posicoes pa-
res sao o dobro da posicoo correspondente no original e as
posicoes impares o triplo.

Exemplo
k = [3, 4, 5, ...]
l = [6, 12, 10, ...]'''

j = 30 # input('tamanho da lista de inteiros: ')

# 'append' alternativo
k = [0]*j  # 'pre-alocacao' de lista
for i in range(j):
    print 'Digite o', i+1, 'o. inteiro: '
    k[i] = input()  # lista original

l = [] # nova lista
for m in range(j):
    if m % 2 == 0:  # se a posicao na lista original, representada pela letra 'm', for par
        l.append(2 * k[m])  # entao o inteiro na posicao correspondente na nova lista valera o dobro
    else:  # senao (posicao na lista original e impar)
        l.append(3 * k[m])  # o inteiro na posicao correspondente na nova lista valera o triplo

print
print 'Posicoes:', j
print 'Lista original de inteiros:', k
print 'Nova lista:', l
