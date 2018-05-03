#   programa que leia o nome completo de uma pessoa,
#   mostrando em seguida o primeiro e o último nome separadamente#

n = str(input("\nDigite seu Nome Completo: ")).strip()
nome = n.split()

print ("\nSeu Primeiro nome é: {} ".format(nome[0]))
print ("Seu Ultimo nome é: {}".format(nome[-1]))


