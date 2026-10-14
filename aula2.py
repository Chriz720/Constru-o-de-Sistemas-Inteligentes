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
