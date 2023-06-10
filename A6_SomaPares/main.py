def main():
    primeiroNumero = int(input("Informe o primeiro número do intervalo: "))
    segundoNumero = int(input("Informe o segundo número do intervalo: "))

    resultado = 0
    for i in range(primeiroNumero, segundoNumero):
        if i%2 == 0:
            resultado += i

    print("Soma dos números pares: " + str(resultado))

if __name__ == "__main__":
    main()