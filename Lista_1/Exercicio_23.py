# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. #


print('\nLEITOR DE NÚMEROS ATÉ 9999 ')
n = int(input('\nDigite um número de 0 até 9999:\n '))
print('Unidade = {}'.format(n % 10))
print('Dezena = {}'.format((n // 10) % 10))
print('Centena = {}'.format((n // 100) % 10))
print('Milhar = {}'.format(n // 1000))


