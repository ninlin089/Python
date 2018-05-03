#  Calcular Multa, se o carro ultrapassar 80km, ele deverá pagar 7,00 por km acima do limite  #


print("\nPROGRAMA DA MULTA")

km = int(input("Quantos Km/h o carro se encontra?  "))
if km > 80:
    print("EXCESSO DE VELOCIDADE em {} !!! Multa a pagar: R${:.2f}"
          .format((km - 80) , ((km - 80)*7)))
else:
    print("Não existe excesso de velocidade")