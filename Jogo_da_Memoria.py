import numpy as np
from random import sample
import os
import time

Acabou_Jogo = False
cont = 0
Posicoes_Abertas = []
Tentativas = 1

matriz_inicial = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
matriz_inicial = sample(matriz_inicial,16)

matriz_inicial = np.reshape(matriz_inicial,(4,4))


Pares_Escondidos = ['*']*16
Reseta_Jogo = ['*']*16

Pares_Escondidos = np.reshape(Pares_Escondidos,(4,4))

print('**** JOGO DA MEMÓRIA ****')
time.sleep(1.8)

print(Pares_Escondidos)

while Acabou_Jogo == False:
    Escolhe_Posicao = int(input('Escolha a primeira posição[x,y]: '))
    x1 = Escolhe_Posicao // 10 % 10
    y1 = Escolhe_Posicao // 1 % 10

    while x1 > 3 or y1 > 3 or Escolhe_Posicao in Posicoes_Abertas:
        Escolhe_Posicao = int(input('Posição inválida ou ja aberta. Escolha a primeira posição[x,y]: '))
        x1 = Escolhe_Posicao // 10 % 10
        y1 = Escolhe_Posicao // 1 % 10
        if x1 <= 3 and y1 <= 3 and Escolhe_Posicao not in Posicoes_Abertas:
            Pares_Escondidos[x1][y1] = matriz_inicial[x1][y1]
            print(Pares_Escondidos)

    Pares_Escondidos[x1][y1] = matriz_inicial[x1][y1]
    print(Pares_Escondidos)

    Escolhe_Posicao2 = int(input('Escolha a segunda posição[x,y]: '))
    x2 = Escolhe_Posicao2 // 10 % 10
    y2 = Escolhe_Posicao2 // 1 % 10

    while x2 > 3 or y2 > 3 or Escolhe_Posicao2 in Posicoes_Abertas or Escolhe_Posicao == Escolhe_Posicao2:
        Escolhe_Posicao2 = int(input('Posição inválida ou ja aberta. Escolha a primeira posição[x,y]: '))
        x2 = Escolhe_Posicao2 // 10 % 10
        y2 = Escolhe_Posicao2 // 1 % 10
        if x2 <= 3 and y2 <= 3 and Escolhe_Posicao2 not in Posicoes_Abertas and Escolhe_Posicao != Escolhe_Posicao2:
            Pares_Escondidos[x2][y2] = matriz_inicial[x2][y2]
            print(Pares_Escondidos)

    Pares_Escondidos[x2][y2] = matriz_inicial[x2][y2]
    print(Pares_Escondidos)

    if int(matriz_inicial[x1][y1]) == int(matriz_inicial[x2][y2]):
        Pares_Escondidos[x1][y1] = matriz_inicial[x1][y1]
        Pares_Escondidos[x2][y2] = matriz_inicial[x2][y2]
        cont += 1
        Posicoes_Abertas.append(Escolhe_Posicao)
        Posicoes_Abertas.append(Escolhe_Posicao2)
        print(Pares_Escondidos)
        print('Parabéns! Você acertou!')

    if int(matriz_inicial[x1][y1]) != int(matriz_inicial[x2][y2]):
        Pares_Escondidos[x1][y1] = '*'
        Pares_Escondidos[x2][y2] = '*'
    Tentativas += 1

    if cont == 8:
        Acabou_Jogo = True
        print('Parabéns! Você conseguiu descobrir todas as casas em', Tentativas, 'jogadas!')
        Pares_Escondidos = Reseta_Jogo
    time.sleep(2)
    os.system('cls') or None
