#input() serve para o usuário trazer informações no código
nome = input("Digite o seu nome: ")

print(f"Olá {nome}! Seja bem-vindo(a)!")

# #tudo será sempre uma string no input()
idade = input("Digite sua idade: ")

print(idade)
print(type(idade))

#primeira forma de conversão
idade_texto = input("Digite sua idade: ")
idade = int(idade_texto)

print(f"Tipo de variável 'idade_texto': {type(idade_texto)}")
print(f"Tipo da variável 'idade': {type(idade)}")
print()
print("No próximo aniversário você terá", idade + 1, "anos.")

#segunda forma
idade = int(input("Digite sua idade: "))
print(f"Tipo da variável 'idade': {type(idade)}")
print()
print("No próximo aniversário você terá", idade + 1, "anos.") 

preco = float(input("Preço do produto: "))
quantidade = int(input("Quantidade: "))

total = preco * quantidade

print("Total da compra:", total)

#isso se chama expressão booliana
idade = 20

print(idade >= 18)

""" ==	Igual a	5 == 5	True
!=	Diferente de	5 != 5	False
>	Maior que	8 > 3	True
<	Menor que	8 < 3	False
>=	Maior ou igual a	7 >= 7	True
<=	Menor ou igual a	4 <= 2	False """

resposta = input("Deseja continuar? Digite sim ou não: ")

print(resposta == "sim")

#if funciona como um "se"
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você atingiu a maioridade.")

print("Consulta encerrada.")

#easter egg
from datetime import datetime

dia = datetime.today().strftime('15/10/2026')

if dia == '15/10/2026':
    print('Feliz Dia dos Professores!') 
 

#elif funciona como uma alternativa extra
media = float(input("Digite a média de 0 a 10: "))

if media >= 7:
    print("Aprovado.")
elif media >= 5:
    print("Em recuperação.")
else:
    print("Reprovado.") 

#and significa e: as duas condições precisam ser verdadeiras.
idade = int(input("Idade: "))
vagas = int(input("Vagas disponíveis: "))

if idade >= 14 and vagas > 0:
    print("Inscrição permitida.")
else:
    print("Inscrição não permitida.") 

#or significa ou: basta que pelo menos uma condição seja verdadeira.
categoria = input("Categoria (estudante, professor ou visitante): ")

if categoria == "estudante" or categoria == "professor":
    print("Desconto disponível.")
else:
    print("Sem desconto.") 

#ao misturar and e or, use parênteses para explicitar o agrupamento desejado:
idade = 16
categoria = "estudante"

if idade >= 14 and (categoria == "estudante" or categoria == "professor"):
    print("Pode participar da atividade.")
else:
    print("Não pode participar da atividade.")

#not significa não. Ele transforma True em False e False em True.
resposta = input("O robô está em manutenção? (sim/nao): ")
em_manutencao = resposta == "sim"

if not em_manutencao:
    print("Robô disponível para uma missão.")
else:
    print("Aguarde o fim da manutenção.")

#podemos fazer uma segunda decisão dentro da primeira. Isso é chamado de aninhamento.
quantidade = int(input("Quantidade desejada: "))
estoque = 10

if quantidade > 0:
    if quantidade <= estoque:
        estoque = estoque - quantidade
        print("Pedido confirmado.")
        print("Estoque restante:", estoque)
    else:
        print("Estoque insuficiente.")
else:
    print("A quantidade deve ser maior que zero.")

