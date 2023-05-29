from A19_ScrabbleScore.calculoScore import calculoScore


def main():
    print("Bem Vindo ao programa que calcula o SCORE de uma palavra")
    palavra = input("Informe uma palavra: ")

    calculoScore(palavra)

if __name__ == "__main__":
    main()