#  Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem,
#  cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas. #

km = int(input("\nDigite quantos Km de distância seu destino possui: "))

if km <=200:
    print("\nSua viagem tem {}km e você terá de pagar: R${:.2f}".format(km, km * 0.50))
else:
    print("\nSua viagem tem {}km e você terá de pagar: R${:.2f}".format(km, km * 0.45))