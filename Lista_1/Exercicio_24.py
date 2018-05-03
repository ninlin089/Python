#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cid = str(input('\nDigite o nome da cidade desejada: ')).upper()

vr = cid.split()
if vr[0] == 'SANTO':
    print('Sua cidade começa com santo!')
else:
    print('Sua cidade não começa com santo!')