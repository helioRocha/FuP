#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
16) Faça um programa que recebe uma lista de uma quantidade
de elementos digitada pela usuário e mostre os valores na
ordem inversa.

Exemplo
o = [1, 2, 3]
n = [3, 2, 1]
'''

# Lista original
q = int(raw_input('quantidade de elementos: '))
if q == 0:
    # 'append' alternativo (conhecido o tamanho da lista)
    original = []*q  # 'pre-alocacao' de lista (original)
    print 'lista vazia'
elif q == 1:
    # 'append' alternativo
    original = [0]*q  # 'pre-alocacao' de lista (original)
    original[0] = int(raw_input('Digite um elemento (numero inteiro): '))
elif q > 1:
    original = []
    for i in range(q):  
        original.append(int(raw_input('Digite um elemento (numero inteiro): ')))

# 'append' alternativo
nova = [0] * len(original)  # 'pre-alocacao' de lista (lista nova)

j = len(original) - 1  # contador atuando sobre a lista original
c = 0  # contador atuando sobre a lista nova
while j >= 0:
    nova[c] = original[j]
    j -= 1  # contador (decrescente) atuando sobre a lista original
    c += 1  # contador (crescente) atuando sobre a lista nova

print
print 'Quantidade de elementos da lista:', q
print 'Lista original:', original
print 'Lista invertida:', nova

###########################################################
'''
# Lista original
q = input('quantidade de elementos: ')
# 'append' alternativo
o = [0]*q # 'pre-alocacao' de lista
for i in range(q):
    o[q] = input('Digite um numero inteiro: ')

j = len(o) - 1
n = [0]*len(o)
c = 0
while j >= 0:
    n[c] = o[j]
    j-=1
    c+=1'''