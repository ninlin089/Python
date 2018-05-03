# Mostrar o maior e menor valor entre 3 numeros digitados #

print("\nInsira abaixo três numeros")
n1 = int(input(''))
n2 = int(input(''))
n3 = int(input(''))

lista = [n1, n2, n3]

print('O maior número é: {}'.format(max(lista)))
print('O menor número é: {}'.format(min(lista)))