# Faca  um programa que leia a largura e a altura de uma parede em
# metros, calcule a sua área e a quantidade de tinta necessária para
# pintá-los, sabendo que cada litro de tinta, pinta uma área de 2 m².


largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura
Litinta = area / 2

print("Área da parede: {}".format(area))
print("Tinta necessária: {0:.0f}Litros".format(Litinta))