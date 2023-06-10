def main():
    numeroInformado = int(input("Informe um número: "))

    numeroAntecessor = 0
    numeroAtual = 1
    guardarNumeroAtual = 0
    sequenciaNumeros = []

    while numeroAtual <= numeroInformado:
        sequenciaNumeros.append(numeroAtual)
        guardarNumeroAtual = numeroAtual
        numeroAtual = numeroAntecessor+numeroAtual
        numeroAntecessor = guardarNumeroAtual

    print("Sequência: " + str(sequenciaNumeros))

if __name__ == '__main__':
    main()