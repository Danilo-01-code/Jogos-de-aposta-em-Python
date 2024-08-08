from cartas import *
import random
from time import sleep
from titulo import *
import sys


cash = 500 
aposta = 0 
passe = 0
def main():
    global cash
    global aposta
    escrevagrande("BLACKJACK")
    print(f'Você possui {cash} R$')
    while True:
        try:
            aposta = float(input('Quanto deseja apostar ? '))
            if aposta > cash or aposta <= 0:
                print('Aposta Inválida')
                continue
            cash -= aposta
            c = str(input(f'Sua aposta foi de R${aposta}, pressione qualquer botão para começar o BLACKJACK: '))
            game()
            break
        except ValueError:
            print('Entrada Inválida')


def sortearcartas():
    carta_sorteada = random.choice(list(cartas.keys()))
    carta_valor = cartas[carta_sorteada]
    return carta_sorteada, carta_valor

def player(Valor_jogador, mao_jogador, first = False, game = False):
    if not isinstance(Valor_jogador, list):
        raise ValueError("Valor_jogador deve ser uma lista.")
    carta, valor = sortearcartas()
    mao_jogador.append((carta, valor))
    Valor_jogador.append(valor)
    if game:
        sleep(0.5)
        print(f"A carta sorteada foi {carta}")
    if first:
        carta1, valor1 = sortearcartas()
        mao_jogador.append((carta1, valor1))
        Valor_jogador.append(valor1)
    return mao_jogador

def Ásverification(som, Valor_jogador):
    cont = 0
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
  
    
def game():
    Ás = False
    Ás_dealer = False
    Valor_dealer = []
    Valor_jogador = []
    mao_dealer = []
    mao_jogador = []
    player(Valor_jogador, mao_jogador, True)  
    print(f'\nSuas cartas são:\n')
    sleep(0.5)
    som = somdealer = 0

    for carta, valor in mao_jogador:
        if valor == 11:
            Ás = True
        print(f'{carta} ', end='')

    som = sum(Valor_jogador)
    if Ás:
        som, Valor_jogador = Ásverification(som, Valor_jogador)
    sleep(0.5)

    print(f'\nValor total do jogador: {som}\n')
    sleep(0.5)
    player(Valor_dealer,mao_dealer, True)
    print(f'\nAs cartas do dealer são:\n')

    for carta, valor in mao_dealer:
        if valor == 11:
            Ás_dealer = True

    somdealer = sum(Valor_dealer)

    if Ás_dealer:
        somdealer, Valor_dealer = Ásverification(somdealer, Valor_dealer)
    print(f'{mao_dealer[0][0]} e uma carta virada para baixo.')
    sleep(0.5)
    print(f'\nValor da carta do dealer {somdealer - mao_dealer[1][1]}\n')
    sleep(0.5)
    if som == 21:
        print('Você fez BLACKJACK!')
        virarcartas(somdealer, Valor_jogador)
    c = str(input('Pressione qualquer botão para continuar: '))
  
    choice(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer,Valor_dealer, Valor_jogador)
    


def choice(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador):
    global passe

    print(f"\nTurno do jogador\n")
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
                hit(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador)

            elif escolha == 1:
                sleep(0.5)
                print(f'\nVocê permanece com a mão:\n') 
                for carta, valor in mao_jogador:
                    print(f'{carta} ', end='')
                sleep(0.5)
                print(f'\nE com o valor: {som}\n')
                sleep(0.5)
                passe += 1
                if passe >= 2:
                    print("\nHora de Virar a carta do dealer\n")
                    sleep(0.5)
                    virarcartas(somdealer, Valor_jogador)
                dealer(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador)

            elif escolha == 2:
                aposta, cash = doubledown()
                hit(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador)

            else:
                print('Valor Inválido.')
                continue
        except ValueError:
            print('Valor Inválido')
            continue        
        dealer(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador)


def dealer(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador):
    global passe
    #I.A do Dealer
    print(f'\nTurno do Dealer\n')
    rng = random.randint(0, 100)
    if somdealer >=19:
        passe +=1
        print('O dealer decidiu manter as suas cartas.')
        if passe >= 2:
            print("Hora de Virar a carta do dealer")
            sleep(0.5)
            virarcartas(somdealer, Valor_jogador)
    if somdealer >= 17:
        if rng >= 75:
            print("O dealer decidiu pegar mais uma carta")
            sleep(2)
            hit(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador, player_play = False)
        else:
            print(passe)
            passe +=1
            print('O dealer decidiu manter as suas cartas.')
            if passe >= 2:
                print("Hora de Virar a carta do dealer")
                sleep(0.5)
                virarcartas(somdealer, Valor_jogador)
            
            choice(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador)
    elif somdealer >= 14:
        if rng >=55:
            print("O dealer decidiu pegar mais uma carta")
            sleep(2)
            hit(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador, player_play = False)
        else:
            passe+=1
            print("O dealer decidiu manter as suas cartas")
            if passe >= 2:
                print("Hora de Virar a carta do dealer")
                sleep(0.5)
                virarcartas(somdealer, Valor_jogador)

            choice(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador)

    else:
        print("O dealer decidiu pegar mais uma carta")
        hit(passe,mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador, player_play = False)

def virarcartas(somdealer, Valor_jogador):
    global cash
    global aposta
    sleep(0.5)
    #ALERTA DE GAMBIARRA
    som = sum(Valor_jogador)
    print(f'\nO jogador fez {som} e o dealer fez {somdealer}\n')
    if somdealer == som:
        print('O jogo Empatou!')
        cash+=aposta
        continuar()
    elif som == 21:
        cash = cash + (aposta * 2)
        print('O jogador Venceu !')

    elif somdealer > 21 and som <= 21:
        cash = cash + (aposta * 2)
        print('Dealer estorou e o Jogador venceu!')
        continuar()

    elif som < 21:
        if som > somdealer:
            cash = cash + (aposta * 2)
            print("O jogador Venceu!")
            continuar()
        else:
            print('O Jogador Perdeu!')

    elif somdealer == 21:
        print('O Jogador Perdeu!')

    elif som > 21:
        print(f'\nVocê excedeu 21, e perdeu imediatamente.\n')

    sleep(0.5)
    if cash <= 0:
        print('Você foi a falência WOMP WOMP')
        escrevavermelho('FIM DE JOGO')
        sys.exit()
    continuar()

    



def continuar():
    global cash
    sleep(1)
    print(f'\nDinheiro atual: {cash}\n')
    while True:
        try:
            con = str(input('Deseja continuar jogando ? [S/N] ')).strip().upper()
            if con == 'N':
                sys.exit()
            elif con == 'S':
                main()
                break
            else:
                print('Entrada Inválida')
        except ValueError:
            print('Entrada Inválida.')

       
def hit( mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador, player_play = True):
    global passe
    passe = 0
    if player_play:
        player(Valor_jogador, mao_jogador, first = False, game = True)
        
        for carta, valor in mao_jogador:
            if valor == 11:
                Ás = True

        som = sum(Valor_jogador)
        sleep(2)
        if Ás:
            som, Valor_jogador = Ásverification(som, Valor_jogador)
        print(f"Valor total do jogador: {som}")
        sleep(2)
        if som > 21:
            virarcartas(somdealer, Valor_jogador)
        else:
            dealer(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador)
    else:
        player(Valor_dealer, mao_dealer, first = False, game = True)
        for carta, valor in mao_dealer:
            if valor == 11:
                Ás_dealer = True

        somdealer = sum(Valor_dealer)  
        sleep(1)
        if Ás:
            somdealer, Valor_jogador = Ásverification(somdealer, Valor_dealer)
        print(f"Valor do dealer: {somdealer - mao_dealer[1][1]} (e uma carta virada para baixo)")
        sleep(1)
        choice(mao_jogador, mao_dealer,som, somdealer, Ás, Ás_dealer, Valor_dealer, Valor_jogador)



def doubledown():
    global cash
    global aposta
    print("Você escolheu dobrar a aposta.")
    sleep(0.5)
    aposta *= 2
    if aposta > cash:
        print("Entretanto você não possui dinheiro o suficiente para dobrar a sua aposta atual")
        aposta/=2
        sleep(4)
    else:
        print(f"Agora sua aposta é: {aposta}")
    return aposta, cash


main()