def main():
    print("Bem-vindo ao programa que calcula o Ajuste Salarial")
    salario = float(input("Informe o Valor de um Salario: "))
    percentual = float(input("Informe o percentual de reajuste salarial: "))
    novo_salario = CalcularSalario(salario, percentual)
    print("\n------------------------------------", end="")
    print("\nSALARIO INICIAL   :", salario, end="")
    print("\nPERCENTUAL AUMENTO:", percentual,"%", end="")
    print("\nNOVO SALARIO      :", novo_salario, end="")
    print("\n------------------------------------", end="")

def CalcularSalario(salario, percentual):
    return salario + (salario * percentual / 100)

if __name__ == "__main__":
    main()