# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade  de dias pelos quais foi alugado. Calcule o preco a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por Km rodado.

print("\nALUGUEL DE CARROS\n")
dia_alg = int(input("Quantidade de dias alugado: "))
km_alg = float(input("Quantidade de Km percorridos: "))

print("Preço por dias alugado: R${}".format(dia_alg*60))
print("Preço Km percorridos:   R${:.2f}".format(km_alg*0.15))
print("Total a pagar: R${:.2f}".format((dia_alg * 60)+(km_alg * 0.15)))