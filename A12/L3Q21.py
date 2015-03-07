#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
21) Faca um programa que receba o nome de cinco produtos e
seus respectivos preços, armazene os em duas listas separa-
das, uma para os produtos e outra para os precos. O progra-
ma deve calcular e mostrar:
* A quantidade de produtos com preco inferior a R$ 50,00;
* O nome dos produtos com preco entre R$ 50,00 e R$100,00;
* A media dos precos dos produtos com preco superior a
  R$ 100,00.
'''

nome = [] # lista contendo nomes dos produtos
preco = [] # lista contendo precos dos produtos

# contadores
preco_inferior = 0
faixa_preco = 0
qtde_sup = 0
soma_sup = 0

# INPUT ###################################################
for i in range(5):
    print 'Produto', i + 1
    nome.append(raw_input('Nome do produto: '))
    preco.append(input('Preco do produto: '))
    print

# PROCESS/OUPUT ###########################################
for j in range(5):
    if preco[j] < 50.00:
        preco_inferior += 1

print 'Quantidade de produtos com preco inferior a R$ 50,00:', preco_inferior
print
if preco_inferior == 0:
    print 'Nenhum dos produtos apresenta preco infeior a R$ 50,00.'
    print
        
print 'Nome dos produtos com preco entre R$ 50,00 e R$ 100,00: '
print

for k in range(5):    
    if (preco[k] >= 50.00) and (preco[k] <= 100.00):
        faixa_preco += 1
        print nome[k], '(custa R$', round(preco[k], 2), ')'

if faixa_preco == 0:
    print 'Nenhum dos produtos apresenta preco entre R$ 50,00 e R$ 100,00.'

for m in range(5):
    if preco[m] > 100.00:
        qtde_sup += 1
        soma_sup += preco[m]
    
#print 'soma do preco dos produtos com valor superior a R$ 100,00:', soma_sup
#print 'quantidade de produtos com valor superior a R$ 100,00:', qtde_sup
print
if qtde_sup > 0:
    print 'Media dos precos dos produtos com preco superior a R$ 100,00:', float(soma_sup)/qtde_sup
else:
    print 'Consta que nenhum produto apresenta preco superior a R$ 100,00.'