# Mostrar um valor digitado em centimetros e milimetros #
# quilômetro, hectômetro, decâmetro e decímetro #

metro = float(input('\nQual o valor em metros? '))

print('O valor em {} convertido para quilometro é {} km'.format(metro, metro/1000))
print('O valor em {} convertido para hectômetro é {} hm'.format(metro, metro/100))
print('O valor em {} convertido para decâmetro é {} dam'.format(metro, metro/10))
print('O valor em {} convertido para dencimetro é {} dm'.format(metro, metro*10))
print('O valor em {} convertido para centímetro é {} cm'.format(metro, metro*100))
print('O valor em {} convertido para milímetro é {} mm'.format(metro, metro*1000))
