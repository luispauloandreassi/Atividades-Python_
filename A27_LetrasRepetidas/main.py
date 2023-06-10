def main():
    palavra = input("Informe uma palavra: ")

    arrayLetras = []

    for letra in palavra:
        arrayLetras.append(letra)

    letraNaoRepetida = ''
    letraNaoRepetidaEncontrada = False

    for i in range(len(palavra)):
        if arrayLetras.count(palavra[i]) == 1:
            letraNaoRepetida = palavra[i]
            letraNaoRepetidaEncontrada = True
            break

    if letraNaoRepetidaEncontrada:
        print("A primeira letra não repetida na palavra é: " + letraNaoRepetida)
    else:
        print("Não existe alguma letra que não se repete na palavra informada.")

if __name__ == '__main__':
    main()