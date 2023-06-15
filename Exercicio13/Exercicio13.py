distancia_km = float(input("Digite a distância percorrida pelo projétil (em quilômetros): "))

tempo_min = float(input("Digite o tempo de percurso do projétil (em minutos): "))

velocidade = (distancia_km * 1000) / (tempo_min * 60)

print("A velocidade do projétil é:", velocidade, "metros por segundo")