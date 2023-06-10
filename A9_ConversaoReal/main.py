def main():
    cotacao = float(input("Informe a cotação do dólar: "))
    saldoDisponivel = float(input("Informe o saldo disponível: "))

    valorConvertido = saldoDisponivel * cotacao

    print("Valor convertido: " + str(round(valorConvertido, 2)))

if __name__ == "__main__":
    main()