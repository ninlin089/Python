# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo(sem considerar espaços)#
# - Quantas letras tem o primeiro nome.    #


nome = str(input('\nDigite seu nome COMPLETO: '))
print('Seu nome em letras maisculas:', nome.upper())
print('seus nome em letras minsuculas:', nome.lower())
print('Quantidade de letras do seu nome:', len(nome.replace(' ','')))
print('Quantidade de letras do primeiro nome:', len(nome.split()[0]))