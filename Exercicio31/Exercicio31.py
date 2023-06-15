def quebra_linha(frase, colunas):
    palavras = frase.split()
    linha = ""
    linhas_quebradas = []

    for palavra in palavras:
        if len(linha) + len(palavra) <= colunas:
            linha += palavra + " "
        else:
            linhas_quebradas.append(linha.strip())
            linha = palavra + " "

    linhas_quebradas.append(linha.strip())
    return linhas_quebradas

frase = input("Digite a frase: ")
colunas = int(input("Digite a quantidade de colunas: "))

linhas_quebradas = quebra_linha(frase, colunas)

for linha in linhas_quebradas:
    print(linha)
