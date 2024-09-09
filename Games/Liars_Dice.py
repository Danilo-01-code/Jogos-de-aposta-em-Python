from random import randint, shuffle
from Games.titulo import *
from Games.zcores import *
from time import sleep
from collections import Counter
import sys


aposta_j = lance = 0
minimo = 1
quantidade = 5


class Bot:
    def __init__(self, dados_bot, quantidade):
        if dados_bot == 1:
            dados_bot = []
        self.dados_bot = dados_bot
        self.quantidade = quantidade
    

    def playbot0(self,dados_jogador, declare = False):
        global minimo
        global lance
        if declare:
            print(f'\nTurno de {participantes[0]}\n')
            sleep(0.5)
            proxplayer()
        
        rng0 = randint(0,100)
        rng1 = randint(0,100)

        minimo+=1

        if minimo == 1:
            minimo +=1

        if rng1 <=30:
            #O bot decidiu aumentar o lançe minimo
            if minimo < 10:
                minimo+=1
            if rng1 < 10:
                if minimo < 10:
                  minimo+=1

        if rng0 <= 75:
            #O bot decidiu não blefar
            contagem = Counter(self.dados_bot)
            maioria = contagem.most_common(1)[0][0]
            lance = maioria
            print(f"\nO {participantes[-1]} disse que tem {minimo} dados de valor {lance}\n")
            sleep(2)

        else:
            #O bot decidiu blefar
            blefe = randint(1,6)
            lance = blefe
            print(f"\nO {participantes[-1]} disse que tem {minimo} dados de valor {lance}\n")
            sleep(2)

        verificar(dados_jogador)

    
    def playbot1(self, dados_jogador, declare = False): 
        #IA do bot para as próximas rodadas
        #Eu sei, código meio idiota, algum dia eu arrumo
        if declare:
            print(f'\nTurno de {participantes[0]}\n')
            sleep(0.5)
            proxplayer()

        contagem = Counter(self.dados_bot)
        maioria = contagem.most_common(1)[0][0]

        rng1 = randint(0,100)
        if lance == maioria:
            if rng1 <= 10:
                print(f'\n{participantes[-1]} Declarou Spot-on!\n')
                sleep(0.5)
                fimrodada(dados_jogador)
            else: 
                self.playbot0(dados_jogador)

        else:
            if len(dados_jogador) <= 3 or len(bot1.dados_bot) <=3 or len(bot2.dados_bot) <= 3:
                if rng1 <=75:
                    print(f'\n{participantes[-1]} Declarou Blefe!\n')
                    sleep(0.5)
                    fimrodada(dados_jogador, blefe = True)
                else:
                    self.playbot0(dados_jogador)
            else:
                if rng1 <=40:
                    print(f'\n{participantes[-1]} Declarou Blefe!\n')
                    sleep(0.5)
                    fimrodada(dados_jogador, blefe = True)
                else:
                    self.playbot0(dados_jogador)
            
      
    def iterar_dados(self):
        global lance
        cont = 0
        for item in self.dados_bot:
            if item == lance:
                cont+=1
        return cont

bot1 = Bot(1,5)
bot2 = Bot(1,5)     

participantes = ["jogador", "bot1", "bot2"]

def main():
    escrevaunderline("BEM VINDO AO LIARS DICE!")
    c = (input(f"\n{cores['underline']}Pressione qualquer botão para jogar: {cores['limpa']}"))
    game()


def game():
    global minimo
    global participantes

    minimo = 1
    game0 = True
    game1 = True

    if quantidade == 0:
        print(f"\nO jogador foi eliminado!\n")
        escrevavermelho("FIM DE JOGO!")
        sleep(0.5)
        sys.exit()
    
    if bot1.quantidade == 0 and bot2.quantidade == 0:
        print(f"\nO jogador ganhou a partida!\n")
        escrevagrande("GAME WIN!")
        sleep(0.5)
        sys.exit()

    if bot1.quantidade == 0:
        if game0:
            print(f"\nO bot1 foi eliminado!\n")
            game0 = False

        participantes.clear()
        participantes = ["jogador", "bot2"]
        
    if bot2.quantidade == 0:
        if game1:
            print(f"\nO bot2 foi eliminado!\n")
            game1 = False

        participantes.clear()
        participantes = ["jogador", "bot1"]
    

    bot1.dados_bot.clear() 
    bot2.dados_bot.clear()
    dados_jogador = []
    
    dados_jogador = distribuirdados(dados_jogador)
    distribuirdadosbot(bot1)
    distribuirdadosbot(bot2)

    turnos()
    sleep(0.5)
    print(f'\nOs dados dos participantes foram sorteados')
    sleep(0.5)
    print(f'Os seus dados são: {dados_jogador}\n')
    sleep(0.5)
    if participantes[0] == "bot1":
        bot1.playbot0(dados_jogador,declare = True)

    elif participantes[0] == "bot2":
        bot2.playbot0(dados_jogador,declare = True)

    else:
        play0(dados_jogador, declare = True)


def distribuirdados(lista):
    global quantidade

    # Verifica se a quantidade é maior que o tamanho atual da lista
    while len(lista) < quantidade:
        lista.append(randint(1, 6))  # Adiciona um número aleatório entre 1 e 6 à lista

    return lista


def distribuirdadosbot(bot):
    while len(bot.dados_bot) < bot.quantidade:
        bot.dados_bot.append(randint(1, 6))


def play1(dados_jogador, declare = False):
    if declare:
        print(f"\nTurno de Jogador\n")
        sleep(0.5)
        proxplayer()

    print(
        """
        [0]BLEFE
        [1]DECLARAR APOSTA
        [2]SPOT-ON
        """
          )
    while True:
        try:
            opc0 = int(input(f"\nSua escolha: \n"))
            if opc0 == 0:
                fimrodada(dados_jogador, blefe = True)
                break
            elif opc0 == 1:
                play0(dados_jogador)
                break
            elif opc0 == 2:
                fimrodada(dados_jogador)
                break
            else:
                print("Entrada Inválida.")
        except ValueError:
            print("Entrada Inválida.")


def play0(dados_jogador, declare = False):
    global lance
    global minimo

    if declare:
        print(f"\nTurno de Jogador\n")
        sleep(0.5)
        proxplayer()

    print(f"\nOs seus dados são: \n")
    print(dados_jogador)
    while True:
        try:
            lance = int(input("Qual o valor do dado você deseja apostar? "))
            if lance > 6 or lance < 1:
                print("Entrada Inválida (valores de 1 a 6 somente)")
            else:
                break
        except ValueError:
            print("Entrada Inválida")
        
    while True:
        try:
            #O valor de opc1 deve ser maior que o mínimo somente se o mínimo for maior que 1, cao contrário poderá ser maior ou igual
            opc1 = int(input(f"Quantos dados desse valor tem na mesa ? (minimo = {minimo}) "))
            if minimo == 1:
                if opc1 >= 1:
                    break
            elif opc1 <= minimo:
                print("Sua aposta deve ser maior que o mínimo ")
            elif minimo > 10:
                print("O valor não pode ser maior que 10.")
            else:
                break
        except ValueError:
            print("Entrada Inválida")
    
    minimo = opc1

    print(f"\nO Jogador disse que tem {minimo} dados de valor {lance}\n")

    verificar(dados_jogador)


def fimrodada(dados_jogador, blefe = False): 
    global minimo
    global lance
    global quantidade

    print(f"\nMostrando os dados dos jogadores:\n")
    sleep(0.5)

    spoton = False

    cont = 0 
    if bot1.quantidade > 0:
        cont += bot1.iterar_dados()
        print(bot1.dados_bot)

    if bot2.quantidade > 0: 
        cont += bot2.iterar_dados()
        print(bot2.dados_bot)
    

    for item in dados_jogador:
        if item == lance:
            cont+=1
   
    print(dados_jogador)
    sleep(2)
    print(f"\nExistem {cont} dados de valor {lance}\n")
    sleep(0.5)
    if blefe:
        if cont >= minimo:
            print(f"\nBlefe inválido!\n")
            sleep(0.5)
            perdeu = True
        else:
            print(f"\nBlefe válido!\n")
            perdeu = False
            sleep(0.5)
    else:
        if cont == minimo:
            print(f"\nSpot-on válido!\n")
            sleep(0.5)
            spoton = True
            perdeu = False
        else:
            print(f"\nSpot-on Inválido!\n")
            sleep(0.5)
            perdeu = True

    if perdeu:
        print(f"\n{participantes[-1]} perdeu um dado\n")
        sleep(0.5)

        if participantes[-1] == "bot1":
            bot1.quantidade -= 1

        elif participantes[-1] == "bot2":
            bot2.quantidade -=1

        else:
            quantidade -=1
    else: #Solução provisória
        if len(participantes) >= 3:
            print(f"\n{participantes[1]} perdeu um dado\n")
            sleep(0.5)
            if spoton:
                #spoton faz com que o outro jogador na mesa (caso ainda não esteja eliminado) perca um dado.
                #Solução provisória
                print(f"\n{participantes[0]} perdeu um dado\n")
                if participantes[0] == "bot1":
                    bot1.quantidade -= 1

                elif participantes[0] == "bot2":
                    bot2.quantidade -=1

                else:
                    quantidade -=1

            if participantes[1] == "bot1":
                bot1.quantidade -= 1

            elif participantes[1] == "bot2":
                bot2.quantidade -=1

            else:
                quantidade -=1
        else:
            print(f"\n{participantes[0]} perdeu um dado\n")
            sleep(0.5)

            if participantes[0] == "bot1":
                bot1.quantidade -= 1

            elif participantes[0] == "bot2":
                bot2.quantidade -=1

            else:
                quantidade -=1

    print(f"\nComeçando nova rodada\n")
    game()



def turnos():
    global participantes
    shuffle(participantes)


def verificar(dados_jogador):
    if participantes[0] == "jogador":
        play1(dados_jogador, declare = True)

    elif participantes[0] == "bot2":
        bot2.playbot1(dados_jogador, declare = True)

    else:
        bot1.playbot1(dados_jogador, declare = True)


def proxplayer():
    global participantes
    #Define quem será o próximo jogador
    primeiro_item = participantes.pop(0)
    participantes.append(primeiro_item)
    



main()