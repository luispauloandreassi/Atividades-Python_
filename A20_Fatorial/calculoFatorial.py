import sys


def calculaFatorial(numero):
    if numero < 0:
        print("-----------------------------------")
        print("     E R R O !!! Está escrito \033[1;4m POSITIVO \033[0m, Você leu \033[1;4m negativo \033[0m???")
        print("     Não é possível calcular fatorial de número negativo!!!")
        print("     Por esse motivo, o programa está sendo finalizado...")

        sys.exit()
    elif numero == 0:
        print("-----------------------------------")
        print("FATORIAL CALCULADO: 1")
    else:
        fatorial = 1.0
        for i in range(1, int(numero) + 1):
            fatorial *= i

        print("-----------------------------------")
        print("     FATORIAL CALCULADO:", fatorial)