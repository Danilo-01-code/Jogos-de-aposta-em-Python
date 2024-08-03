from cartas import *
import random
from time import sleep
from titulo import *

escrevagrande("BLACKJACK")

def sortearcartas():
    carta_sorteada = random.choice(list(cartas.keys()))
    carta_valor = cartas[carta_sorteada]
    return carta_sorteada, carta_valor

def player(mao_jogador, first=False):
    carta, valor = sortearcartas()
    mao_jogador.append((carta, valor))
    if first:
        carta1, valor1 = sortearcartas()
        mao_jogador.append((carta1, valor1))
    return mao_jogador

def Ás():

    
def game():
    mao_jogador = []
    player(mao_jogador, True)  
    print('')
    print('Suas cartas são:')
    print('')
    som = 0
    for carta, valor in mao_jogador:
        print(f'{carta} ', end='')
        som += valor
    print('')
    print(f'Valor total: {som}')
    print('')
    # print(
    #     """
    #     [0] HIT
    #     [1] STAND
    #     [2] DOUBLE DOWN
    #     [3] SPLIT
    #     [4] SURRENDER
    #     [5] INSURANCE
    #     [6] EVEN MONEY
    #     """
    # )
    

game()