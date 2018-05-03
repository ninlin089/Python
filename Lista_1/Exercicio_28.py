#  O usuario tentará adivinhar um numero sorteado entre 0 e 5 pela Máquina  #

from random import *

num_aleatorio = randint(0,5)

print("\nBem- vindo ao jogo da adivinhação! ")
print("\nTente Descobrir o numero que nosso computador escolheu de 0 até 5")
num_user = int(input("\nDigite um Numero de 0 a 5: "))


if num_aleatorio == num_user:
    print("\,Parabens, você é bom mesmo :D")
else:
    print("\nNão foi dessa vez, :( ")
    print("Numero que você escolheu {} e o numero da maquina {}"
          .format(num_user,num_aleatorio))
