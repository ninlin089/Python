# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. #


print('-='*20)
print('         Formador de triangulos')
print('-='*20)

sega = float(input("\nDigite o 1º Segmento: "))
segb = float(input("Digite o 2º Segmento: "))
segc = float(input("Digite o 3º Segmento: "))

primeiro = (segb - segc) < sega < segb + segc
segundo  = (sega - segc) < segb < sega + segc
terceiro = (sega - segb) < segc < sega + segb


if primeiro and segundo and terceiro:
    print ("\nESSES SEGMENTOS PODEM FORMAR UM TRIÂNGULO")
else:
    print ("\nESSES SEGMENTOS NÃO PODEM FORMAR UM TRIÂNGULO")