import re

def ConverteRomano(algarismos):
    deParaRomanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    valorInteiro = 0
    for i in range(len(algarismos)):
        valor = deParaRomanos[algarismos[i]]
        if i + 1 < len(algarismos) and valor < deParaRomanos[algarismos[i + 1]]:
            valorInteiro -= valor
        else:
            valorInteiro += valor

    return valorInteiro

def validarAlgarismosRomanos(algarismos):
    correto = re.compile(r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
    return correto.match(algarismos) is not None