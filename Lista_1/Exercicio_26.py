#  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a
# letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a
# última vez.  #


a = str(input("\nInsira uma frase ")).strip().upper()
print ("\nNa sua frase, a letra A apareceu {} vezes, sendo {} minúsculas e {} maiúsculas."
       .format(a.count('A') + a.count('a')  + a.count('À') + a.count("à"),
               a.count('a') + a.count("à") , a.count('A') + a.count('À')))
print("A letra 'A' aparece 1º Na posição: {}".format(a.find('A') + 1))
print("E por ultimo Na posição: {}"          .format(a.rfind('A')+ 1))