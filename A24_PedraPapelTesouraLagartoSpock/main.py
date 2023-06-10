def main():
    print("-----Bem-vindo ao LagartoSpock-----")

    primeiroJogador = input("Informe o nome do 1° jogador: ")
    segundoJogador = input("Informe o nome do 2° jogador: ")

    print(primeiroJogador + ", escolha uma opção: ")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("4 - Lagarto")
    print("5 - Spock")
    opcaoPrimeiroJogador = int(input())

    print(segundoJogador + ", escolha uma opção: ")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("4 - Lagarto")
    print("5 - Spock")
    opcaoSegundoJogador = int(input())

    resultado = ""
    if opcaoPrimeiroJogador == opcaoSegundoJogador or opcaoSegundoJogador == opcaoPrimeiroJogador:
        resultado = "O jogo empatou!"
    elif opcaoPrimeiroJogador == 1 and (opcaoSegundoJogador == 3 or opcaoSegundoJogador == 4):
        resultado = "O jogador "+primeiroJogador+" ganhou."
    elif opcaoPrimeiroJogador == 2 and (opcaoSegundoJogador == 1 or opcaoSegundoJogador == 4):
        resultado = "O jogador "+primeiroJogador+" ganhou."
    elif opcaoPrimeiroJogador == 3 and (opcaoSegundoJogador == 2 or opcaoSegundoJogador == 4):
        resultado = "O jogador "+primeiroJogador+" ganhou."
    elif opcaoPrimeiroJogador == 4 and (opcaoSegundoJogador == 2 or opcaoSegundoJogador == 5):
        resultado = "O jogador "+primeiroJogador+" ganhou."
    elif opcaoPrimeiroJogador == 5 and (opcaoSegundoJogador == 1 or opcaoSegundoJogador == 3):
        resultado = "O jogador "+primeiroJogador+" ganhou."
    else:
        resultado = "O jogador "+segundoJogador+" ganhou."

    print(resultado)

if __name__ == "__main__":
    main()