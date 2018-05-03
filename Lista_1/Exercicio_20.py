# Sortear nomes em ordem #

import random

nome1 = str(input("\nDigite o 1º Nome: "))
nome2 = str(input("Digite o 2º Nome: "))
nome3 = str(input("Digite o 3º Nome: "))
nome4 = str(input("Digite o 4º Nome: "))
nome5 = str(input("Digite o 5º Nome: "))

LISTA = [nome1, nome2 , nome3, nome4, nome5]
random.shuffle(LISTA)

print("Nome sorteados em ordem: ")
print(LISTA)