from random import randint, shuffle
from titulo import *
from zcores import *
from time import sleep
from collections import Counter
import sys


#Liars dice project

#Declarar Blefe,Declarar Spot on, entrar com aposta

aposta_j = lance = 0
minimo = 1
turno = ''
quantidade = 5
class Bot:
    def __init__(self, dados_bot, quantidade, eliminado):
        if dados_bot == 1:
            dados_bot = []
        self.dados_bot = dados_bot
        self.quantidade = quantidade
        self.eliminado = eliminado

    def verificar_eliminado(self):
        if self.quantidade <= 0:
            self.eliminado = True
        else:
            self.eliminado = False


    def playbot0(self,dados_jogador):
        global minimo
        global lance
    
        print(f'\nTurno de {participantes[0]}\n')
        sleep(0,5)

        proxplayer()
        
        rng0 = randint(0,100)
        rng1 = randint(0,100)

        if rng1 <=30:
            #O bot decidiu aumentar o lançe minimo
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

        verificar(participantes,dados_jogador)

    
    def playbot1(self, dados_jogador): 
        #IA do bot para as próximas rodadas
        print(f'\nTurno de {participantes[0]}\n')
        sleep(0,5)

        contagem = Counter(self.dados_bot)
        maioria = contagem.most_common(1)[0][0]

        rng1 = randint(0,100)
        if lance == maioria:
            if rng1 <= 10:
                print(f'\n{participantes[0]} Declarou Spot-on!\n')
                sleep(0,5)
                fimrodada(dados_jogador)
            pass     
        else:

            pass  
      
    def iterar_dados(self,cont):
        global lance

        for item in self.dados_bot:
            if item == lance:
                cont+=1
        return cont

bot1 = Bot(1,5,False)
bot2 = Bot(1,5,False)     

participantes = ["jogador", "bot1", "bot2"]

def main():
    escrevaunderline("BEM VINDO AO LIARS DICE!")
    c = (input(f"\n{cores['underline']}Pressione qualquer botão para jogar: {cores['limpa']}"))
    game()


def game():
    global participantes

    bot1.verificar_eliminado
    bot2.verificar_eliminado

    if quantidade == 0:
        print(f"\nO jogador foi eliminado!\n")
        escrevavermelho("FIM DE JOGO!")
        sleep(0,5)
        sys.exit()

    if bot1.eliminado and bot2.eliminado:
        print(f"\nO jogador ganhou a partida!\n")
        escrevagrande("GAME WIN!")
        sleep(0,5)
        sys.exit()

    if bot1.eliminado:
        participantes = ["jogador", "bot2"]
        
    if bot2.eliminado:
        participantes = ["jogador", "bot1"]
    

    bot1.dados_bot.clear() 
    bot2.dados_bot.clear()
    dados_jogador = []
    
    distribuirdados(dados_jogador)
    distribuirdadosbot(bot1)
    distribuirdadosbot(bot2)

    turnos(participantes)
    sleep(0,5)
    print(f'\nOs dados dos participantes foram sorteados')
    sleep(0,5)
    print(f'Os seus cinco dados são: {dados_jogador}\n')
    sleep(0,5)
    if participantes[0] == "bot1":
        bot1.playbot0(dados_jogador)

    elif participantes[0] == "bot2":
        bot2.playbot0(dados_jogador)

    else:
        play(dados_jogador)


def distribuirdados(listas):
    global quantidade

    for lista in listas:
        while len(lista) < quantidade:
            lista.append(randint(1, 6))


def distribuirdadosbot(bot):
    global quantidade

    while len(bot.dados_bot) < quantidade:
        bot.dados_bot.append(randint(1, 6))


def play():
    print(f"\nTurno de Jogador\n")
    sleep(0,5)
    print(
        """
        [0]BLEFE
        [1]DECLARAR APOSTA
        [2]SPOT-ON
        """
          )


def fimrodada(dados_jogador, blefe = False):
    global minimo
    global lance
    global quantidade

    print(f"\nMostrando os dados dos jogadores:\n")
    sleep(0,5)

    cont = 0
    if bot1.eliminado == False:
        cont += bot1.iterar_dados(cont)
        print(bot1.dados_bot)

    if bot2.eliminado == False:
        cont += bot2.iterar_dados(cont)
        print(bot2.dados_bot)

    #lembre-se de fazer iteração dos dados do jogador
    print(dados_jogador)
    sleep(2)
    print(f"\nExistem {cont} dados de valor {lance}\n")
    sleep(0,5)
    if blefe:
        if cont >= minimo:
            print(f"\nBlefe inválido!\n")
            sleep(0,5)
            perdeu = True
        else:
            print(f"\nBlefe válido!\n")
            perdeu = False
            sleep(0,5)
    else:
        if cont == minimo:
            print(f"\nSpot-on válido!\n")
            sleep(0,5)
            perdeu = False
        else:
            print(f"\nSpot-on Inválido!\n")
            sleep(0,5)
            perdeu = True

    if perdeu:
        print(f"\n{participantes[0]} perdeu um dado\n")
        sleep(0,5)

        if participantes[0] == "bot1":
            bot1.quantidade -= 1

        elif participantes[0] == "bot2":
            bot2.quantidade -=1

        else:
            quantidade -=1
    else:
        print(f"\n{participantes[-1]} perdeu um dado\n")
        sleep(0,5)

        if participantes[-1] == "bot1":
            bot1.quantidade -= 1

        elif participantes[-1] == "bot2":
            bot2.quantidade -=1

        else:
            quantidade -=1

    print(f"\nComeçando nova rodada\n")



def turnos():
    global participantes

    shuffle(participantes)


def verificar(dados_jogador):
    if participantes[0] == "player":
        play(dados_jogador)

    elif participantes[0] == "bot2":
        bot2.playbot1(dados_jogador)

    else:
        bot1.playbot1(dados_jogador)


def proxplayer():
    global turno
    global participantes
    #Define quem será o próximo jogador
    primeiro_item = participantes.pop(0)
    participantes.append(primeiro_item)
    turno = participantes[0]



main()