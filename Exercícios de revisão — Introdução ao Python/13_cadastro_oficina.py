nome_da_oficina = "Robótica para iniciantes"
sala = "Laboratório 2"
quantidade_de_vagas = 24
duração_em_horas = 2.5
inscrições_abertas = True

print("=====OFICINA=====")
print("Nome da oficina:", nome_da_oficina)
print("Sala:", sala)
print("Quantidade de vagas:", quantidade_de_vagas)
print("Duração em horas:", duração_em_horas)
print("Inscrições abertas:", inscrições_abertas)
print("==================")

print("Nome da oficina:", type(nome_da_oficina))
#é uma string, ela representa o nome da oficina.
print("Sala:", type(sala))
#é uma string, ele representa a localização da oficina.
print("Quantidade de vagas:", type(quantidade_de_vagas))
#é um número real, ele representa a quantidade de vagas disponíveis na oficina.
print("Duração em horas:", type(duração_em_horas))
#é um valor booleano, ele representa a duração da oficina em horas.
print("Inscrições abertas:", type(inscrições_abertas))
#é um valor booleano, ele representa se as inscrições estão abertas ou não.