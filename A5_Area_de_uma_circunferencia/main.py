import math


def main():
    pi = 3.14159265
    print("Bem-vindo ao programa que calcula Circunferencia")

    raio = float(input("Informe o valor do raio: "))
    print("-------------------------------------------",end="")
    print("\n     Para o Valor de Raio", raio, "\n     Temos a Circunferencia:", CalcularCircunferencia(pi, raio))

def CalcularCircunferencia(pi, raio):
    return math.pow(raio, 2) * pi

if __name__ == "__main__":
    main()