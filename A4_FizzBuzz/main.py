import sys
from A4_FizzBuzz.fizzBuzz import FizzBuzz

def main():
    print("Bem-vindo ao programa FizzBuzz, segue a regra: ")

    print("          -Números divisíveis por 3 devem aparecer no console como Fizz ao invés do número")
    print("          -Números divisíveis por 5 devem aparecer como Buzz ao invés do número")
    print("          -Números divisíveis por 3 e 5 devem aparecer como FizzBuzz ao invés do número\n")

    print("Favor informar um intervalo de números:")
    numeroInicial = int(input("Número Inicial: "))
    numeroFinal = int(input("Número Final: "))

    if numeroFinal <= numeroInicial:
        print("E-R-R-O!!! Numero Final é menor ou Igual ao Numero Inicial.")
        print("O programa está sendo finalizado!!!!")
        sys.exit()
    else:
        FizzBuzz(numeroInicial, numeroFinal)

if __name__ == "__main__":
    main()