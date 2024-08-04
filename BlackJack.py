from cartas import *
import random
from time import sleep
from titulo import *

escrevagrande("BLACKJACK")

def sortearcartas():
    carta_sorteada = random.choice(list(cartas.keys()))
    carta_valor = cartas[carta_sorteada]
    return carta_sorteada, carta_valor

def player(mao_jogador, first=False,):
    carta, valor = sortearcartas()
    mao_jogador.append((carta, valor))
    if first:
        carta1, valor1 = sortearcartas()
        mao_jogador.append((carta1, valor1))
    return mao_jogador

def Ásverification(som):
    if som > 21:
        som -=10
        return som
    else:
        return som
    
def game():
    Ás = False
    Ás_dealer = False
    mao_dealer = []
    mao_jogador = []
    player(mao_jogador, True)  
    print('')
    print('Suas cartas são:')
    print('')
    som = somdealer = 0
    for carta, valor in mao_jogador:
        if valor == 11:
            Ás = True
        print(f'{carta} ', end='')
        som += valor

    if Ás:
        som = Ásverification(som)

    print('')
    print(f'Valor total do jogador: {som}')
    print('')
    player(mao_dealer, True)
    print('')
    print('As cartas do dealer são: ')
    print('')
    for carta, valor in mao_dealer:
        if valor == 11:
            Ás_dealer = True
        somdealer += valor

    if Ás_dealer:
        somdealer = Ásverification(somdealer)
    print(f'{mao_dealer[0][0]} e uma carta virada para baixo.')
    print('')
    print(f'Valor da carta do dealer {somdealer - mao_dealer[1][1]}')
    c = str(input('Pressione qualquer botão para continuar'))
    #choice()
    


#def choice(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer)
    # print(
    #     """
    #     [0] HIT
    #     [1] STAND
    #     
    #     """
    # )
    

game()