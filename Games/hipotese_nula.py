import scipy.stats as stats
import numpy as np
from time import sleep
import sys


def hipotese_nula(array):
    print(array,"\n")
    while True:
        try:
            h0 = float(input("Digite qual é a sua hipótese: "))
        except ValueError:
            print("Valor Inválido\n")
        else:
            break
    print("")
    return h0


def again(array):
    print(
        """
        [0] Criar uma nova amostra.
        [1] Testar uma nova hipótese com a mesma amostra
        [2] Sair
        """
        )
    while True:
        try:
            opc = int(input(""))
            print("")
            
        except ValueError:
            print("Entrada Inválida.\n")

        if opc == 0:
            main()

        elif opc == 1:
            h0 = hipotese_nula(array)
            statistic_t, p_value = hipotese(h0,array)
            res(statistic_t,p_value, array)

        else:
            sys.exit()


def hipotese(h0,array):
    statistic_t, p_value = stats.ttest_1samp(array,h0)
    return statistic_t, p_value 


def main():
    print("\nTente adivinhar qual é a média dessa amostra:\n")

    array = np.random.randint(0, 100, 50)
    h0 = hipotese_nula(array)
    statistic_t, p_value = hipotese(h0,array)
    res(statistic_t,p_value, array)


def res(statistic_t,p_value, array):
    print(f"O valor da estatística t é: {statistic_t}\n")
    
    if statistic_t < 0:
        print("é provável que a média amostral é menor que a média hipotética.\n")
    elif statistic_t > 0:
        print("é provável que a média amostral é maior que a média hipotética.\n")

    if p_value < 0.05:
        print(f"Se a hipótese nula fosse verdadeira, haveria {round(p_value*100,4)}% de chance de observar uma média amostral tão extrema.\n")
        sleep(2)
        print("A hipótese nula foi rejeitada.\n")
        sleep(1)

    else:
        print(f"A probabilidade de observar essa média amostral considerando que a hipótese nula é verdadeira, é de: {round(p_value*100,4)}%\n")
        sleep(2)
        print("Não há evidências para rejeitar a hipótese nula\n")
        sleep(1)
        
    again(array)


main()
