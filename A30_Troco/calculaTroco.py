def calcularCedulasMoedasTroco(valor):
    troco = {}

    valores = [100, 50, 10, 5, 1, 0.5, 0.1, 0.05, 0.01]

    for vlr in valores:
        qtd = int(valor / vlr)
        if qtd > 0:
            troco[vlr] = qtd
            valor -= qtd * vlr

    return troco