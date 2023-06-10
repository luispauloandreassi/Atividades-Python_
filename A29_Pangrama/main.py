def main():
    frase = input("Informe uma frase: ")

    arrayLetras = []

    for letra in frase:
        if letra not in arrayLetras:
            arrayLetras.append(letra)

    if len(arrayLetras) == 26:
        print("A frase informada é um pangrama.")
    else:
        print("A franse informada não é um pangrama.")

if __name__ == '__main__':
    main()