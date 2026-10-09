nome = "Atlas"
energia = 100
distancia_percorrida = 0
amostras_coletadas = 0
missao_em_andamento = True

print("=====FICHA INICIAL=====")
print("Nome:", nome)
print("Energia:", energia)
print("Distância percorrida, em metros:", distancia_percorrida)
print("Amostras coletadas:", amostras_coletadas)
print("Missão em andamento", missao_em_andamento)
print("=======================\n")

print("=====REGISTRO DE MISSÃO=====")
distancia_percorrida = 120
energia = energia - 80
print("O robô percorre", distancia_percorrida, "metros e consome", energia, "pontos de energia.")
amostras_coletadas = 3
energia = energia - 5
print("Coleta", amostras_coletadas, "amostras e consome", energia, "pontos de energia.")
energia = energia - 5
print("Recarrega", energia, "pontos de energia.")
distancia_percorrida = 80
energia = energia + 15
print("Percorre mais", distancia_percorrida, "metros e consome", energia, "pontos de energia.")
amostras_coletadas = 2
energia = energia - 15
print("Coleta mais", amostras_coletadas, "amostras e consome", energia, "pontos de energia.")
missao_em_andamento = False
print("Missão em andamento:", missao_em_andamento)
print("================================")

metros_por_minuto = 200 / 4
print("Metros por minuto:", metros_por_minuto)