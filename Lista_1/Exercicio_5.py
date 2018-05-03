#Mostrar o Antecessor e Sucessor de uma número#

n1 = int(input("Digite um número: "))

sucessor = n1 + 1
antecessor = n1 - 1

print("")
print("Antecessor de {}: {}".format(n1, antecessor))
print("Sucessor de {}: {}".format(n1, sucessor))