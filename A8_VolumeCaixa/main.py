def main():
    comprimento = float(input("Informe o comprimento: "))
    largura = float(input("Informe a largura: "))
    altura = float(input("Informe a altura: "))

    volume = comprimento * largura * altura
    print("O volume da caixa é: " + str(volume))

if __name__ == "__main__":
    main()