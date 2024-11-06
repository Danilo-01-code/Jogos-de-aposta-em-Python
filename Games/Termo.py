from Games.zcores import cores
import sys
from Games.termowords import palavras
from random import randint

class Termo:

    def __init__(self, resposta,green = 0):
        self.resposta = resposta
        self.green = green

    def palavra(self, res):
        global i

        if res.isalpha() == False:
            print("Somente caracteres.")
            i-=1
            return main
        
        if len(res) != len(self.resposta):
            print("A palavra deve conter 5 letras.")
            i-=1
            return main
                
        for j in range(len(res)):
            passe = True
            usado = ''
            if res[j] == self.resposta[j]:
                print(f"{cores['verde']}{res[j]}{cores['limpa']}", end="")
                self.green +=1
                usado+= res[j]
                passe = False

            if passe:
                self.green = 0
                for k in range(len(self.resposta)):
                    if passe:
                        if self.resposta[k] == res[j]:
                            if res[j] not in usado:
                                print(f"{cores['amarelo']}{res[j]}{cores['limpa']}", end="")
                                usado += res[j]
                                passe = False
               
            if res[j] != self.resposta[j] and passe:
                print(f"{cores['vermelho']}{res[j]}{cores['limpa']}", end="")

        print("\n")

    def win(self):
        if self.green >= 5:
            print(f"{cores['verde']}{'VOCÊ GANHOU !'}{cores['limpa']}")
            sys.exit()
        if i == 6:
            print(f"{cores['vermelho']}{'VOCÊ PERDEU !'}{cores['limpa']}")
            print(f"A PALAVRA ERA: {cores['verde']}{self.resposta}{cores['limpa']}")
            sys.exit()

i = 0

def main():
    global i 

    termo1 = Termo(palavras[randint(0,99)])

    while True:
        res = str(input("")).lower()
        i+=1

        termo1.palavra(res)
        termo1.win()

if __name__ == "__main__":
    main()