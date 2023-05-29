def calculoScore(palavra):

    # Conveftendo em Maiúscula para atendimento de ser Case Insensitive
    palavra_maiuscula = palavra.upper()
    score = 0

    for letra in palavra_maiuscula:
        if letra in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']:
            score += 1
        elif letra in ['D', 'G']:
            score += 2
        elif letra in ['B', 'C', 'M', 'P']:
            score += 3
        elif letra in ['F', 'H', 'V', 'W', 'Y']:
            score += 4
        elif letra == 'K':
            score += 5
        elif letra in ['J', 'X']:
            score += 8
        elif letra in ['Q', 'Z']:
            score += 10

    print("-----------------------------------")
    print("   SCORE CALCULADO:", score)