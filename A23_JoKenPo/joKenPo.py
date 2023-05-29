import sys


def juizJoKenPon(jogador1, jogador2):
    if jogador1 == jogador2:
        print("     QUE PENA! OCORREU EMPATE!")
    elif jogador1 == "Pedra" and jogador2 == "Tesoura":
        print("     JOGADOR 1 VENCEU!!!")
    elif jogador1 == "Papel" and jogador2 == "Pedra":
        print("     JOGADOR 1 VENCEU!!!")
    elif jogador1 == "Tesoura" and jogador2 == "Papel":
        print("     JOGADOR 1 VENCEU!!!")
    else:
        print("     JOGADOR 2 VENCEU!!!")

def converteOpcoes(opcao):
    if opcao == "1":
        return "Pedra"
    elif opcao == "2":
        return "Papel"
    elif opcao == "3":
        return "Tesoura"
    else:
        return "Invalido"