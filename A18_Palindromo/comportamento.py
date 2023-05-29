def invertDados(dados):
    # EM GO UTILIZEI 10 LINHAS!!!
    # :: percorre a String toda e o -1 significa em ordem invertida.
    return dados[::-1]

def verificaPalindromo(dados, dadosInvertidos):
    if dados == dadosInvertidos:
        print("RESULTADO: É PALINDROMO!!!")
    else:
        print("RESULTADO: NÃO É PALINDROMO!!!")