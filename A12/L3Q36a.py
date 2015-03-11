#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
 36) Faca um programa para voce jogar com um amigo o jogo
 da velha. Voce deve criar uma matriz em que cada valor
 deve  ser “X” ou “O” e seu programa deve dizer quem e o
 jogador  vencedor. Para fazer a verificacao de vitoria seu
 programa  deve verificar as diagonais principal e
 secundaria e tambem cada linha e coluna.'''

v = [[], [], []]  # criar matriz do jogo
for i in range(3):  # com 3 linhas
    for j in range(3):  # e 3 colunas
        # indicacao das posicoes para as possibilidades de jogada
        v[i].append((i, j))

print 'Jogo da velha'
print
print '_O_|_O_|_X_'
print '_O_|_!_|_X_'
print ' X | X | O '
print
print 'Carregando o jogo...'
# apresentacao da matriz original do jogo
print v[0]
print v[1]
print v[2]
print

k = 0  # alternador (entre jogadores) E contador da partida
while k < 10:  # excede o numero maximo de jogadas
    if k == 9:  # k igual a nove eh superior ao numero maximo de jogadas
        print 'Empate!'  # neste caso, ninguem venceu, logo, havera um empate
        break
### Jogador X ##################################################################
    else:
        if k % 2 == 0:  # pro-v alternancia entre jogadores
            print 'joga X; jogada', k + 1
            ###print 'Aviso: para nao perder a vez, evite jogada repetida!'
            print
            # escolha da linha
            i = input('escolha a posicao da linha no jogo [0, 1, 2]: ')
            # escolha da coluna
            j = input('escolha a posicao da coluna no jogo [0, 1, 2]: ')
            # nao estando ocupada a posicao escolhida...
            if (v[i][j] != ' X  ') and (v[i][j] != '  O '):
                v[i][j] = ' X  '  # ...joga X ###(estando ocupada, perde a vez)
            else:  # caso contrario, o jogador devera escolher outra posicao para que o jogo continue
                while (v[i][j] == ' X  ') or (v[i][j] == '  O '):
                    print
                    print 'posicao ocupada, escolha outra:'
                    print
                    # escolha da linha
                    i = input('escolha a posicao da linha no jogo [0, 1, 2]: ')
                    # escolha da coluna
                    j = input('escolha a posicao da coluna no jogo [0, 1, 2]: ')
                v[i][j] = ' X  '  # ...joga X
            # todas as condicoes para a vitoria de X
            if (v[0][0] == v[0][1] == v[0][2] == ' X  ') or \
               (v[1][0] == v[1][1] == v[1][2] == ' X  ') or \
               (v[2][0] == v[2][1] == v[2][2] == ' X  ') or \
               (v[0][0] == v[1][0] == v[2][0] == ' X  ') or \
               (v[0][1] == v[1][1] == v[2][1] == ' X  ') or \
               (v[0][2] == v[1][2] == v[2][2] == ' X  ') or \
               (v[0][0] == v[1][1] == v[2][2] == ' X  ') or \
               (v[0][2] == v[1][1] == v[2][0] == ' X  '):
                print
                print 'X venceu!'
                print  # A matriz atualizada e apresentada
                print v[0]
                print v[1]
                print v[2]
                break
            else:  # nao havendo vitoria, o jogo continua
                print  # A matriz atualizada e apresentada
                print v[0]
                print v[1]
                print v[2]
                print
                k += 1  # sera a vez do proximo jogador (O)
                
### Jogador O ##################################################################
        else:
            print 'joga O, jogada', k + 1
            ###print 'Aviso: para nao perder a vez, evite jogada repetida!'
            print
            # escolha da linha
            i = input('escolha a posicao da linha no jogo [0, 1, 2]: ')
            # escolha da coluna
            j = input('escolha a posicao da coluna no jogo [0, 1, 2]: ')
            # nao estando ocupada a posicao escolhida...
            if v[i][j] != ' X  ' and v[i][j] != '  O ':
                v[i][j] = '  O '  # ...joga O ###(estando ocupada, perde a vez)
            else:  # caso contrario, o jogador devera escolher outra posicao para que o jogo continue
                while (v[i][j] == ' X  ') or (v[i][j] == '  O '):
                    print
                    print 'posicao ocupada, escolha outra:'
                    print
                    # escolha da linha
                    i = input('escolha a posicao da linha no jogo [0, 1, 2]: ')
                    # escolha da coluna
                    j = input('escolha a posicao da coluna no jogo [0, 1, 2]: ')
                v[i][j] = '  O '  # ...joga O
            # todas as condicoes para a vitoria de O
            if (v[0][0] == v[0][1] == v[0][2] == '  O ') or \
               (v[1][0] == v[1][1] == v[1][2] == '  O ') or \
               (v[2][0] == v[2][1] == v[2][2] == '  O ') or \
               (v[0][0] == v[1][0] == v[2][0] == '  O ') or \
               (v[0][1] == v[1][1] == v[2][1] == '  O ') or \
               (v[0][2] == v[1][2] == v[2][2] == '  O ') or \
               (v[0][0] == v[1][1] == v[2][2] == '  O ') or \
               (v[0][2] == v[1][1] == v[2][0] == '  O '):
                print
                print 'O venceu!'
                print  # A matriz atualizada e apresentada
                print v[0]
                print v[1]
                print v[2]
                break
            else:  # nao vencendo O, o jogo continua
                print  # A matriz atualizada e apresentada
                print v[0]
                print v[1]
                print v[2]
                print
                k += 1  # sera a vez do proximo jogador (X)
