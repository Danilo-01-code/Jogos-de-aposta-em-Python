from random import randint
from Games.zcores import cores
import sys

record = 0
def main(record):
    pontos = 0
    print(f'{cores["vermelho"]}-={cores["limpa"]}'*20)
    print(f'{"Pega-Pega Mortal":^40}')
    print(f'{cores["vermelho"]}-={cores["limpa"]}'*20)
    while True:
        try:
            play = str(input('Deseja Jogar? [S/N]: ')).upper()
            if play == 'S':
                munição = -1
                hp = 101
                game(munição,hp, pontos, record)
            elif play == 'N':
                return gameover(pontos, record)
            else:
                print('Digite [S/N] ')
        except ValueError:
            print('Entrada Inválida')
        


def game(munição, hp, pontos, record):
    if munição == 0:
        print('Sua munição acabou')
        return gameover(pontos, record)
    esconderijos = ("Dentro Guarda-Roupa","Em baixo da cama", "Dentro da Geladeira","De baixo da mesa","De baixo da pia")
    rng = esconderijos[randint(0,4)]
    print('')
    print(f"Pontos atuais {pontos}")
    print('')
    print(f"O escondedor agora está {rng}, onde deseja mirar com a sua sniper?")
    print(
        """
        [0] Cabeça
        [1] Torso
        [2] Pernas
        [3] Braços
        """

        )
    while True:
        try:
            escolha = int(input("Sua escolha: "))
            if escolha > 3 or escolha < 0:
                print('Valor Inválido')
            death(escolha, rng, pontos, record, munição, hp)
            break
        except ValueError:
            print('Valor inválido')
            


def death(escolha, rng, pontos, record, munição, hp):
    pontosatual = 0
    death_c = 0
    if munição == -1:
        munição = randint(3,6)
    print('')
    print(f"Você tem {munição} munição restantes")
    print('')
    munição -= 1
    if hp == 101:
        hp = 100
    if rng == "Dentro Guarda-Roupa":
        death_c+= -4
    elif rng == "Em baixo da cama":
        death_c+= -7
    elif rng == "Dentro da Geladeira":
        death_c+= -9
    elif rng == "De baixo da mesa":
        death_c+= 6
    elif rng == "De baixo da pia":
        death_c+= 7
    if escolha == 0:
        death_c+=10
        if randint(0,100)<= death_c:
            pontosatual += 100
            pontos += pontosatual
            hp = 0
            print(f'Você acertou a cabeça dele, sangue voou para todo o lado, {pontosatual} pontos')
        else:
            errou(munição, hp, pontos, record)
    elif escolha == 1:
        death_c+= 30
        if randint(0,100) <= death_c:
            if randint(1,3) == 1:
                pontosatual+=60
                hp = 0
                pontos += pontosatual
                print(f'Você perfurou o tiro no peito e o matou, mais {pontosatual} pontos')
            else:
                pontosatual+=40
                hp-=40
                pontos += pontosatual
                if hp <= 0:
                    print(f'Você acertou e o matou, ele não aguentou os ferimentos. Mais {pontosatual} pontos.')
                else:
                    print(f'Você acertou o tiro entretanto ele ainda está vivo, mais {pontosatual} pontos')
                    game(munição,hp, pontos, record)
        else:
            errou(munição,hp, pontos, record)
    elif escolha == 2:
        death_c+=44
        if randint(0,100) <=death_c:
            hp-=25
            pontosatual+= 30
            pontos += pontosatual
            if hp <= 0:
                print(f'Você acerta a perna e o sangramento excessivo acabou o matando, mais {pontosatual} pontos')
            else: 
                print(f'Você acertou o tiro na perna, Ele permanece vivo. mais {pontosatual} pontos')
                game(munição,hp, pontos, record)
        else:
            errou(munição,hp, pontos, record)
    elif escolha == 3:
        death_c+=40
        if randint(0,100) <=death_c:
            hp -= 30
            pontosatual+= 40
            pontos += pontosatual
            if hp <= 0:
                print(f'Você acerta o braço e o sangramento excessivo acabou o matando, mais {pontosatual}')
            else: 
                print(f'Você acertou o tiro no braço, Ele permanece vivo. mais {pontosatual} pontos')
                game(munição,hp, pontos, record)
        else: 
            errou(munição,hp, pontos, record)
    gamewin(pontos, record, munição)


def gamewin(pontos, record, munição):
    pontos+= munição * 3
    print('')
    print(f'Mais {munição * 3 } pontos por ter finalizado com {munição} munições')
    print('')
    print('Mais 40 pontos por ter conseguido a eliminação.')
    pontos+=40
    print('')
    print(f'Você ganhou o Jogo! com um total de {pontos} pontos')
    print('')
    record = recordgame(pontos, record)
    while True:
        try:
            continuar = str(input("Deseja começar um jogo novo ? [S/N] ")).upper()
            if continuar == 'S':
                main(record)
                break
            elif continuar == 'N':
                print('Volte sempre!')
                sys.exit()
                break
            else:
                print('Digite [S/N] ')
        except ValueError:
            print('Entrada Inválida')
    

def errou(munição,hp, pontos, record):
    print('Você errou o tiro')
    print('')
    print(f'Você tem {munição} munições restantes')
    print('')
    if munição <= 0:
        gameover(pontos,record)
    print('')
    while True:
        try:
            continuar = str(input("Deseja continuar ? [S/N]")).upper()
            if continuar == 'S':
                break
            elif continuar == 'N':
                return gameover(pontos, record)
            else:
                print('Digite [S/N] ')
        except ValueError:
            print('Entrada Inválida')

    game(munição,hp, pontos, record)

def gameover(pontos, record):
    print('Fim de Jogo!')
    print('')
    print(f'Total  de pontos {pontos}.')
    print('')
    record = recordgame(pontos, record)
    while True:
        try:
            continuar = str(input("Deseja começar um jogo novo ? [S/N] ")).upper()
            if continuar == 'S':
                plays = 0
                main(record)
                break
            elif continuar == 'N':
                print('Volte sempre!')
                sys.exit()
                break
            else:
                print('Digite [S/N] ')
        except ValueError:
            print('Entrada Inválida')

def recordgame(pontos,record):
    if pontos > record:
        record = pontos
        print(f'O novo record é de {pontos} pontos!')
    else:
        print(f'O record atual é de {record}') 
    return record


main(record)
