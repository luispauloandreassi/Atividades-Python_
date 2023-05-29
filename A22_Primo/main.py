import math

def main():
    print("Bem vindo ao programa que calcula se um número é primo.")
    print("I N F O R M A Ç Ã O:")
    print("     Número Primo é aquele divisível apenas por 1 e por ele mesmo.")
    numero = int(input("Informe um número inteiro para ser verificado: "))

    if VerificaPrimo(numero):
        print("--------------------------------------")
        print("     => O número", numero, "\033[1;4m É \033[0m primo.")#Formatacao para gerar Negrito e Sublinhado
    else:
        print("--------------------------------------")
        print("     => O número", numero, "\033[1;4m NÃO \033[0m é primo.")

def VerificaPrimo(numero):
    if numero <= 1:
        return False

    verificacao = int(math.sqrt(numero))

    for i in range(2, verificacao + 1):
        if numero % i == 0:
            return False

    return True


if __name__ == "__main__":
    main()