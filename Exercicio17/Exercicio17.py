elementos = []
for i in range(12):
    elemento = int(input("Digite um elemento: "))
    elementos.append(elemento)

elementos.sort(reverse=True)

print("Elementos em ordem decrescente:")
for elemento in elementos:
    print(elemento)
