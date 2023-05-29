import sys

from A21_AlgarismosRomanos.calculaRomanos import validarAlgarismosRomanos, ConverteRomano

def main():
    print("Bem vindo ao programa que converte algarismos romanos.")
    algarismoRomano = input("Informe um Algarismo Romano: ")
    algarismoRomano = algarismoRomano.upper()

    if validarAlgarismosRomanos(algarismoRomano):
        print("--------------------------------------------")
        print("     ALGARISMO ROMANO         :", algarismoRomano)
        print("     INTERIO CORRESPONDENTE   :", ConverteRomano(algarismoRomano))
    else:
        print("--------------------------------------------")
        print("     Algarismo Informado é Inválido!!!")
        print("     O programa esta sendo finalizado...")
        sys.exit()

if __name__ == "__main__":
    main()