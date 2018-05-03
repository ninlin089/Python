# Calcular o novo salário do funcionario.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15% #


salario = float(input("\nDigite o salário do funcionário: R$"))


if salario > 1250:
    aumento = (salario*10)/100
else:
    aumento = (salario*15)/100

print("\nO novo salário será de: R${:.2f}".format(aumento+salario))
