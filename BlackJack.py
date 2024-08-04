from cartas import *
import random
from time import sleep
from titulo import *
import sys

cash = 500 
def main(cash):
    escrevagrande("BLACKJACK")
    print(f'Você possui {cash} R$')
    aposta = float(input('Quanto deseja apostar ? '))
    #TODO
    cash -= aposta
    #TODO


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
    
def game(cash):
    Ás = False
    Ás_dealer = False
    mao_dealer = []
    mao_jogador = []
    player(mao_jogador, True)  
    print('')
    print('Suas cartas são:')
    print('')
    sleep(0.5)
    som = somdealer = 0
    for carta, valor in mao_jogador:
        if valor == 11:
            Ás = True
        print(f'{carta} ', end='')
        som += valor

    if Ás:
        som = Ásverification(som)
    sleep(0.5)
    print('')
    print(f'Valor total do jogador: {som}')
    print('')
    sleep(0.5)
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
    sleep(0.5)
    print('')
    print(f'Valor da carta do dealer {somdealer - mao_dealer[1][1]}')
    sleep(0.5)
    c = str(input('Pressione qualquer botão para continuar'))
    choice(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer)
    


def choice(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer):
    print(
         """
         [0] HIT
         [1] STAND     
         """
     )
    while True:
        try:
            escolha = int(input('Sua escolha: '))
            if escolha == 0:
                player(mao_jogador)
            if escolha == 1:
                sleep(0.5)
                print(f'Você permanece com a mão: {mao_jogador}')
                sleep(0.5)
                print(f'E com o valor: {som}')
                sleep(0.5)
        except ValueError:
            print('Valor Inválido')
            continue
    dealer(mao_dealer, somdealer, Ás_dealer)


def dealer(mao_dealer, somdealer, Ás_dealer):
    #TODO


def virarcartas(somdealer, som, cash, aposta):
    print(f'O jogador fez {som} e o dealerfez {somdealer}')
    print('')
    sleep(0.5)
    if somdealer == 21 and som == 21:
        print('O jogo Empatou!')
        cash+=aposta
    elif som = 21:
        cash = cash + (aposta * 2)
        print('O jogador Venceu !')

    elif somdealer = 21:
        print('O Jogador Perdeu!')

    sleep(0.5)
    print('')
    print(f'Dinheiro atual: {cash}')
    sleep(0.5)
    if cash <= 0:
        print('Você foi a falência WOMP WOMP')
        escrevavermelho('FIM DE JOGO')
        sys.exit()
    else:
        while True:
            try:
                con = str(input('Deseja continuar jogando ? [S/N] ')).strip().upper()
                if con == 'N':
                    sys.exit()
                elif con == 'S':
                    main(cash)
                    break
                else:
                    print('Entrada Inválida')
            except ValueError:
                print('Entrada Inválida.')
        



main(cash)