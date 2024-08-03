from zcores import cores

def escreva(txt):
     """
     Cria um titulo personalizado usando cor Ansi 
     O titulo contem hifens na parte de cima e de baixo do seu texto
     os hifens vao ter o tamanho de len(txt) +4 
    """
    esc = len(txt)+4
    print('-'* esc)
    print(f'  {txt}  ')
    print('-'*esc)

def escrevavermelho(txt):
    """
     Cria um titulo vermelho personalizado usando cor Ansi 
     O titulo contem hifens na parte de cima e de baixo do seu texto
     os hifens vao ter o tamanho de len(txt) +4 
    """
    esc = len(txt)+4
    print('-'* esc)
    print(f'  {cores["vermelho"]}{txt}{cores["limpa"]}  ')
    print('-'*esc)

