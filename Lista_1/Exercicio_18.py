# Faca um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

ang = float(input('\nDigite o ângulo:'))

seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan((math.radians(ang)))

print("\nAngulo: {:.2f}".format(ang))
print("Seno: {:.2f}".format(seno))
print("Cosseno: {:.2f}".format(cosseno))
print("Tangente: {:.2f}".format(tangente))