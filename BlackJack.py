from cartas import *
import random
from time import sleep
from titulo import *
import sys


cash = 500 
def main(cash):
    escrevagrande("BLACKJACK")
    print(f'Você possui {cash} R$')
    while True:
        try:
            aposta = float(input('Quanto deseja apostar ? '))
            if aposta > cash or aposta <= 0:
                print('Aposta Inválida')
                continue
            cash -= aposta
            c = str(input(f'Sua aposta foi de {aposta}R$, pressione qualquer botão para começar o BLACKJACK: '))
            game(cash, aposta)
            break
        except ValueError:
            print('Entrada Inválida')


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

def Ásverification(som, Valor_jogador):
    if som > 21:
        for i,v in enumerate(Valor_jogador):
            if cont == 0: 
                if v == 11:
                    Valor_jogador[i] = 1
                    cont+=1
            elif cont == 1:
                if som > 21: 
                    if v == 11:
                        Valor_jogador[i] = 1
                        cont+=1
        
        som = sum(Valor_jogador)
        return som, Valor_jogador
    else:
        return som ,Valor_jogador
    
def game(cash, aposta):
    Ás = False
    Ás_dealer = False
    Valor_dealer = []
    Valor_jogador = []
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
        Valor_jogador.append(valor)

    som = sum(Valor_jogador)
    if Ás:
        som, Valor_jogador = Ásverification(som, Valor_jogador)
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
        Valor_dealer.append(valor)

    somdealer = sum(Valor_dealer)

    if Ás_dealer:
        somdealer, Valor_dealer = Ásverification(somdealer, Valor_dealer)
    print(f'{mao_dealer[0][0]} e uma carta virada para baixo.')
    sleep(0.5)
    print('')
    print(f'Valor da carta do dealer {somdealer - mao_dealer[1][1]}')
    sleep(0.5)
    if som == 21:
        print('Você fez BLACKJACK!')
        dealer(mao_dealer, somdealer, Ás_dealer, cash, aposta)
    c = str(input('Pressione qualquer botão para continuar: '))
    passe = 0
    choice(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer,Valor_dealer, Valor_jogador,cash, aposta, passe)
    


def choice(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador,cash, aposta, passe):

    print("Turno do jogador")
    sleep(0.5)
    print(
         """
         [0] HIT
         [1] STAND   
         [2] DOUBLE DOWN  
         """
     )
    while True:
        try:
            escolha = int(input('Sua escolha: '))
            if escolha == 0:
                hit(passe, mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador,cash, aposta)

            elif escolha == 1:
                sleep(0.5)
                print(f'Você permanece com a mão: {mao_jogador}')
                sleep(0.5)
                print(f'E com o valor: {som}')
                sleep(0.5)
                passe += 1
                if passe == 2:
                    print("Hora de Virar a carta do dealer")
                    sleep(0.5)
                    virarcartas(somdealer, som, cash, aposta)
                dealer(passe, mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador,cash, aposta)

            elif escolha == 2:
                aposta, cash = doubledown(aposta, cash)
                hit(passe, mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador,cash, aposta)

            else:
                print('Valor Inválido.')
        except ValueError:
            print('Valor Inválido')
            
        dealer(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador,cash, aposta, passe)


def dealer(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador,cash, aposta, passe):
    #I.A do Dealer
    print('')
    print('Turno do Dealer')
    print('')
    rng = random.randint(0, 100)
    if somdealer >= 17:
        if rng >= 75:
            print("O dealer decidiu pegar mais uma carta")
            sleep(2)
            hit(passe, mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador,cash, aposta, player_play = False)
        else:
            passe +=1
            if passe == 2:
                print("Hora de Virar a carta do dealer")
                sleep(0.5)
                virarcartas(somdealer, som, cash, aposta)
            
            choice(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador,cash, aposta,passe)
    elif somdealer >= 14:
        if rng >=55:
            print("O dealer decidiu pegar mais uma carta")
            sleep(2)
            hit(passe, mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador,cash, aposta, player_play = False)
        else:
            passe+=1
            print("O dealer decidiu manter as suas cartas")
            if passe == 2:
                print("Hora de Virar a carta do dealer")
                sleep(0.5)
                virarcartas(somdealer, som, cash, aposta)

            choice(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador,cash, aposta, passe)

    else:
        print("O dealer decidiu pegar mais uma carta")
        hit(passe,mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador,cash, aposta, player_play = False)

def virarcartas(somdealer, som, cash, aposta):
    sleep(0.5)
    if som <= 21:
        print(f'O jogador fez {som} e o dealer fez {somdealer}')
        print('')
    sleep(0.5)
    if somdealer == 21 and som == 21:
        print('O jogo Empatou!')
        cash+=aposta
    elif som == 21:
        cash = cash + (aposta * 2)
        print('O jogador Venceu !')

    elif somdealer == 21:
        print('O Jogador Perdeu!')
    else:
        print('Você excedeu 21, e perdeu imediatamente.')
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

       
def hit(passe, mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador,cash, aposta, player_play = True):
    passe = 0
    if player_play:
        player(mao_jogador)
        print("Você pegou o: ")
        print('')
        res = ''
        for carta, valor in mao_jogador:
            if valor == 11:
                Ás = True
                res+=f'{carta} '
                Valor_jogador.append(valor)
            som = sum(Valor_jogador)
        print(res)
        sleep(2)
        if Ás:
            som, Valor_jogador = Ásverification(som, Valor_jogador)
        print(f"Valor total do jogador: {som}")
        sleep(2)
        if som > 21:
            virarcartas(somdealer, som, cash, aposta)
        else:
            dealer(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador,cash, aposta, passe)
    else:
        player(mao_dealer)
        print("O dealer pegou a carta:")
        print("")
        for carta, valor in mao_dealer:
            if valor == 11:
                Ás_dealer = True
                res+=f'{carta} '
                Valor_dealer.append(valor)
            somdealer = sum(Valor_dealer)
        print(res)
        sleep(2)
        if Ás:
            somdealer, Valor_jogador = Ásverification(somdealer, Valor_jogador)
        print(f"Valor do dealer: {somdealer - mao_dealer[1][1]} (e uma carta virada para baixo)")
        sleep(2)
        choice(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador,cash, aposta, passe)



def doubledown(aposta, cash):
    print("Você escolheu dobra a aposta.")
    sleep(0.5)
    aposta *= 2
    if aposta > cash:
        print("Entretanto você não possui dinheiro o suficiente para dobrar a sua aposta atual")
        aposta/=2
        sleep(4)
    else:
        print(f"Agora sua aposta é: {aposta}")
    return aposta, cash


main(cash)