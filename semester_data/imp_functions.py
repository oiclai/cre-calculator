import os 
import time
# funcao para limpar terminal que arthur mostrou
def clear():
    os.system('clear||cls')
'''
os.system(X): executa o comando fornecido no shell do SO. 
O comando depende do sistema operacional em uso.

clear: (comando) usado em sistemas baseados em Unix (como Linux e macOS) para limpar a tela do terminal.
||: Este operador é usado para executar o próximo comando se o primeiro falhar.
Ele é útil quando você está tentando garantir que, independentemente do sistema operacional, a tela seja limpa.
cls: Este comando é usado em sistemas Windows para limpar a tela do terminal.

>>>> LIMPAR TERMINAL SENDO SO INUX OU WINDOWS <<<<
'''
def twoSecondsPause():
    return time.sleep(2)
def LessThanOneSecondPause():
    return time.sleep(0.8)
def FiveSecondsPause():
    return time.sleep(5)