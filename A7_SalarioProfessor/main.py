def main():
    horasTrabalhadas = float(input("Informe as horas trabalhadas no mês: "))
    horaAula = float(input("Informe o valor da hora-aula: "))
    percentualDesconto = float(input("Informe o percentual de desconto: "))

    salarioBruto = horasTrabalhadas * horaAula
    totalDesconto = salarioBruto * (percentualDesconto / 100)
    salarioLiquido = salarioBruto - totalDesconto

    print("Salário bruto: " + str(salarioBruto) + " | Salário líquido: " + str(salarioLiquido))

if __name__ == "__main__":
    main()