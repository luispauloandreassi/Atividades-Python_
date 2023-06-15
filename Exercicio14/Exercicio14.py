votos_candidato_a = int(input("Digite a quantidade de votos válidos para o candidato A: "))
votos_candidato_b = int(input("Digite a quantidade de votos válidos para o candidato B: "))
votos_candidato_c = int(input("Digite a quantidade de votos válidos para o candidato C: "))

votos_nulos = int(input("Digite a quantidade de votos nulos: "))
votos_brancos = int(input("Digite a quantidade de votos em branco: "))

total_eleitores = votos_candidato_a + votos_candidato_b + votos_candidato_c + votos_nulos + votos_brancos

percent_votos_validos = (votos_candidato_a + votos_candidato_b + votos_candidato_c) / total_eleitores * 100
percent_votos_a = votos_candidato_a / total_eleitores * 100
percent_votos_b = votos_candidato_b / total_eleitores * 100
percent_votos_c = votos_candidato_c / total_eleitores * 100
percent_votos_nulos = votos_nulos / total_eleitores * 100
percent_votos_brancos = votos_brancos / total_eleitores * 100

print("Número total de eleitores:", total_eleitores)
print("Percentual de votos válidos em relação à quantidade de eleitores:", percent_votos_validos, "%")
print("Percentual de votos do candidato A em relação à quantidade de eleitores:", percent_votos_a, "%")
print("Percentual de votos do candidato B em relação à quantidade de eleitores:", percent_votos_b, "%")
print("Percentual de votos do candidato C em relação à quantidade de eleitores:", percent_votos_c, "%")
print("Percentual de votos nulos em relação à quantidade de eleitores:", percent_votos_nulos, "%")
print("Percentual de votos em branco em relação à quantidade de eleitores:", percent_votos_brancos, "%")
