def main():
    continuar = True
    arrayNumeros = []

    while continuar == True:
        numero = int(input("Informe um número: "))

        arrayNumeros.append(numero)

        print("Deseja continuar informando números: ")
        print("1 - Sim.")
        print("2 - Não.")
        continuar = input() == "1"

    somaNumeros = 0.00
    for numero in arrayNumeros:
        somaNumeros += float(numero)

    resultado = somaNumeros / list.count(arrayNumeros)
    print("A média dos números é: " + resultado)

if __name__ == "__main__":
    main()