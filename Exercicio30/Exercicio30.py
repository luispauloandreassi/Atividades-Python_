valor_total = float(input("Digite o valor total a ser pago: "))
valor_pago = float(input("Digite o valor efetivamente pago: "))

troco = valor_pago - valor_total

cedulas = [100, 50, 10, 5, 1]
moedas = [0.5, 0.1, 0.05, 0.01]

troco_em_cedulas_moedas = {}

for cedula in cedulas:
    if troco >= cedula:
        quantidade_cedulas = int(troco // cedula)
        troco_em_cedulas_moedas[cedula] = quantidade_cedulas
        troco -= quantidade_cedulas * cedula

for moeda in moedas:
    if troco >= moeda:
        quantidade_moedas = int(troco // moeda)
        troco_em_cedulas_moedas[moeda] = quantidade_moedas
        troco -= quantidade_moedas * moeda

print("Troco a ser fornecido:", troco)
print("Cédulas e moedas do troco:")
for valor, quantidade in troco_em_cedulas_moedas.items():
    print(f"{quantidade} {'cedula' if valor >= 1 else 'moeda'} de R${valor}")
