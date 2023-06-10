def main():
    primeiroNumero = float(input("Informe o primeiro número: "))
    segundoNumero = float(input("Informe o segundo número: "))
    terceiroNumero = float(input("Informe o terceiro número: "))

    resultadoPrimeiroNumero = primeiroNumero * primeiroNumero
    resultadoSegundoNumero = segundoNumero * segundoNumero
    resultadoTerceiroNumero = terceiroNumero * terceiroNumero
    resultado = resultadoPrimeiroNumero + resultadoSegundoNumero + resultadoTerceiroNumero

    print("A soma dos quadrados é: " + str(resultado))

if __name__ == "__main__":
    main()