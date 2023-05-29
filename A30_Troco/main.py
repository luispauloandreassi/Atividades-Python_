import sys
from A30_Troco.calculaTroco import calcularCedulasMoedasTroco


def main():
    print("Bem vindo ao programa TROCO EFICIENTE: ")
    valorCompra = float(input("Informe o valor da compra: "))
    valorPago = float(input("Informe o valor pago: "))

    # Calculando o valor do Troco
    valor = valorPago - valorCompra

    if valor < 0:
        print("\n-------------------")
        print("      Valor pago menor que a quantidade da compra...")
        print("      Você deveria ter dado mais dinheiro!")
        print("      O programa está sendo finalizado......")
        sys.exit()

    # Chamando a função para retornar a quantidade menor de cédulas/moedas
    troco = calcularCedulasMoedasTroco(valor)

    print("------------------------------------------------------------", end="")
    print(f"\n     Troco Calculado: R${valor:.2f}:")
    print("     Para esse troco, a menor quantidade de Cédulas/Moedas é:")
    for valor, qtd in troco.items():
        if valor < 1.00:
            print(f"     R${valor:.2f} Qtd Moeda(s) -> {qtd}")
        else:
            print(f"     R${valor:.2f} Qtd Cédula(s) -> {qtd}")


if __name__ == "__main__":
    main()