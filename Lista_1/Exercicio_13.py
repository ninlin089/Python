# Faca um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.


salario = float(input("\nDigite o salário do funcionario: "))

novo_sal = salario + (salario*0.15)

print("Novo salário: R${0:.4f}".format(novo_sal))