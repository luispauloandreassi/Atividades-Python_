import sys
from A23_JoKenPo.joKenPo import converteOpcoes, juizJoKenPon

def main():
    print("Bem vindo ao programa JokenPo: ")
    print("Informe o número das opções:")
    print("     1 - Pedra")
    print("     2 - Papel")
    print("     3 - Tesoura")

    jogador1 = input("JOGADOR 1: ")
    opcaoJogador1 = converteOpcoes(jogador1)
    if opcaoJogador1 == "Invalido":
        print("     A T E N C A O!!! Opção inválida - Jogador 1!")
        print("     O programa está sendo finalizado...")
        sys.exit()

    jogador2 = input("JOGADOR 2: ")
    opcaoJogador2 = converteOpcoes(jogador2)
    if opcaoJogador2 == "Invalido":
        print("     A T E N C A O!!! Opção inválida! - Jogador 2!")
        print("     O programa está sendo finalizado...")
        sys.exit()

    print("\n================================ ")
    print("Jogador 1: " + converteOpcoes(jogador1))
    print("Jogador 2: " + converteOpcoes(jogador2))

    juizJoKenPon(converteOpcoes(jogador1), converteOpcoes(jogador2))



if __name__ == "__main__":
    main()