# Conversão de Reais para dolares, euro, libra #


real = float(input("\n Digite o valor em reais a ser convertido: "))

dolar = real / 3.27

print("\nReais: R$ {}".format(real))
print("Dolar: US$ {0:.2f}".format(dolar))
print("Euro:  {0:.2f}€".format(real / 4.18))
print("Libra: £ {0:.2f}".format(real/4.77))