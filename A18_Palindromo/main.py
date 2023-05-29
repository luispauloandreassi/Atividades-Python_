from A18_Palindromo.comportamento import verificaPalindromo, invertDados


def main():
    print("Bem vindo ao programa que verifica se o digitado é um Palindromo!!")
    print("A T E N C A O!!!!\n   >>>> O programa faz diferenciacao entre Letras MAIUSCULAS e minusculas...")
    dados = input("#Informe uma palavra, frase ou número para ser verificado: ")

    print("----------------------------------------------------")
    print("\nVerificando......")

    print("TEXTO INFORMADO: " + dados)
    print("TEXTO INVERTIDO: " + invertDados(dados))
    verificaPalindromo(dados, invertDados(dados))

if __name__ == "__main__":
    main()