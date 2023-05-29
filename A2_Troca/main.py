def main():
    print("Bem-vindo ao programa Troca Troca")
    print("Precisamos de dois valores para continuar...")

    valorA = input("Informe um valor: ")
    valorB = input("Informe outro valor: ")

    print("\n_____Valores Originais:")
    print("Valor1:", valorA)
    print("Valor2:", valorB)

#atribuição múltipla - Da direita para esquerda. Valor de A REcebe B e o valor de B Recebe A
    valorA, valorB = valorB, valorA

    print("\n_____Valores Após a Troca:")
    print("Valor1:", valorA)
    print("Valor2:", valorB)

if __name__ == "__main__":
    main()