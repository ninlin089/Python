# Faça um programa que leia um ano qualquer e mostre se ele é bissexto. #

ano = int(input('Que ano quer analisar? '))
cond1 = ano % 4
cond2 = ano % 100
cond3 = ano % 400
if cond1 == 0:
    if cond2 == 0 and cond3 != 0:
        print(f'O ano {ano} NÃO é BISSEXTO')
    else:
        print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')