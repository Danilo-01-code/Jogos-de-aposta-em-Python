from random import randint
from titulo import escrevavermelho
from AsciiDraws import caveirudo
from time import sleep
import sys


def main():
    escrevavermelho(f'ROLETA RUSSA')
    while True:
        try:
            balas = int(input('Quantas balas deseja colocar na pistola ? (min: 1 max 5) '))
            if balas > 5 or balas < 1:
                print('Número de Balas inválido')
                continue
            else:
                break
        except ValueError:
            print('Entrada Inválida')
            continue
    caveirudo()
    escrevavermelho('ESTÁ PRONTO PARA COMEÇAR ?')
    while True:
        res = str(input('[S/N] ')).upper()
        if res.isalpha():
            if res[0] == 'S':
                break
            elif res[0] == 'N':
                print('Estaremos te esperando, quando estiver pronto...')
                sys.exit()
            else:
                print('Entrada Inválida')
                continue
        else:
            print('Entrada Inválida')
            continue
    tent = False
    pistola(balas, tent)


def pistola(balas, tent):
    if tent:
        while True:
            try:
                bp = int(input('Digite 1 para colocar mais uma bala... '))
                if bp == 1:
                    break
                else:
                    print('Coloque a Bala')
                    continue
            except ValueError:
                print('Coloque logo essa bala')
                continue
        balas+=1
    escrevavermelho('PRESSIONE 0, PARA PUXAR O GATILHO')
    while True:
        try:
            player = int(input(''))
            if player == 0:
                morte = randint(1,6)
                i = 1
                while i < 11:
                    print(i)
                    i+=1
                    sleep(1.2)
                if balas <= morte:
                    sleep(1.2)
                    print('PARABÉNS, VOCÊ SOBREVIVEU')
                    break
                else:
                    morteplayer()
                    break
            else:
                print('Querendo em desistir ? agora é tarde de mais...')
                continue
        except ValueError:
            print('Não tente fugir...')
            continue
    pistolacomputer(balas, tent)


def pistolacomputer(balas, tent):
    print('')
    print('Colocando mais uma bala...')
    print('')
    balas+=1
    escrevavermelho('MY TURN')
    morte = randint(1,6)
    i = 0 
    while i < 11:
        print(i)
        i+=1
        sleep(1.2)
    if balas <= morte:
        sleep(1)
        print('PARABÉNS, PARA MIM! EU SOBREVIVI')
        tent = True
        pistola(balas, tent)
    else:
        gamewin()

def gamewin():
    sleep(1.2)
    escrevavermelho('BANG!!')  
    sleep(1.3)
    print('Você ganhou o jogo.')
    sys.exit()


def continua():
    while True:
        res = str(input('Jogar de novo ? [S/N] ')).upper
        if res.isalpha():
            if res[0] == 'S':
                break
            elif res[0] == 'N':
                print('Foi bom jogar com você.')
                sys.exit()
            else:
                print('Entrada Inválida')
                continue
        else:
            print('Entrada Inválida')
            continue


def morteplayer():
    sleep(1.2)
    escrevavermelho('BANG!!')  
    sleep(1.2)
    print('Sua cabeça estorou e sangue jorrou pra todo o lado Womp Womp.')   
    escrevavermelho('PERDEU BOBÃO!!')
    sys.exit()  


main()