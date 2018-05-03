# Faca um algoritmo que leia o preco de um produto e mostre
# seu novo preço, com 5% de desconto.

preco1 = float(input("\nDigite o preço do produto:"))

preco2 = preco1 - (preco1 *0.05)

print("\nNovo preço com desconto: R${0:.2f}".format(preco2))