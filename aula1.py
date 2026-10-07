#para textos se usa aspas duplas ou simples
print("Bem-vindos ao curso de Sistemas Inteligentes!")
print("Legal")
print("Deslegal")

#para números não se usa aspas, a menos que seja um texto
print(100 + 20)

#vírgula é usada para separar as palavras
print("Christian", "Israel", end=" ")
#end= é para dar espaço ao final para separar as palavras

print("\n--------------------------------------------\n") #\n tem a mesma função de um "enter"

#sep serve para separar as palavras
print("Costa", "Fagundes", sep=" | ")

#operações matemáticas:
print(10 + 5) #é usado para adição
print(20 - 5) #é usado para subtração
print(2 * 5) #é usado para multiplicação
print(10 / 5) #é usado para divisão
print("rs" * 10) #é usado para repetição

print(4 ** 2) #** é usado para potenciação
print(12 ** 0.5) #0.5 é usado para raiz quadrada
print(5 // 2) #// é usado para divisão inteira
print(5 % 2) #% é usado para resto da divisão

#alt+shift+a é usado para comentar várias linhas de uma vez só
#ctrl+; é usado para comentar uma linha de cada vez

nome = "Christian" #a variavel é algo para me referir a algo, e o valor é o que ela representa

#a variavel é usada para armazenar valores, e o print é usado para mostrar esses valores na tela
print(nome) 

#exemplo de variáveis com diferentes tipos de dados:
idade = 19
nacionalidade = "Brasileiro"
ocupacao = "Estudante"
print("Nome:", nome)
print("Idade:", idade, "anos")
print("Nacionalidade:", nacionalidade)
print("Ocupação:", ocupacao)

PI = 3.14159 #constante é um valor que não muda, e é usado para representar valores fixos

print(PI)

#str é usado para representar textos
#int é usado para representar números inteiros
#float é usado para representar números com vírgula
#bool é usado para representar valores booleanos (True ou False)

print(type(nome)) #type é usado para mostrar o tipo de dado da variável

print(type(idade)) #type é usado para mostrar o tipo de dado da variável

print(type(nacionalidade)) #type é usado para mostrar o tipo de dado da variável

print(type(ocupacao)) #type é usado para mostrar o tipo de dado da variável  

#exercício 1
print("\n===== MEU PERFIL =====")

nome = "Christian Israel Costa Fagundes"
cidade = "São Leopoldo - RS"
idade = 19
tecnologia = "IA"

print("Nome:", nome)
print("Cidade:", cidade)    
print("Idade:", idade, "anos")
print("Tecnologia:", tecnologia)

#exercício 2

nome = "Nintendo Switch 2"
preço = 4599.99
quantidade_em_estoque = 100
disponivel = True

print("\n===== PRODUTO =====")
print("Nome:", nome)   
print("Preço:", preço)
print("Quantidade em estoque:", quantidade_em_estoque)
print("Disponível:", disponivel)

#exercício 3

pontos_iniciais = 250

pontos = pontos_iniciais + 100
pontos = pontos - 50
pontos = pontos + 30

print("\n===== PONTOS =====")
print("Pontuação final:", pontos)

#exercício 4

preco = 18.50
quantidade = 4
total = preco * quantidade

print("\n===== COMPRA =====")
print("Valor da compra:", total)

#exercício 5

horas = 7

print("\n===== CONVERSÃO DE HORAS =====")
print(horas, "hora(s) equivale(m) a", horas * 60, "minuto(s)")

#exercício 6

pontos_de_vida = 200

vida = pontos_de_vida - 45
vida = vida - 30
vida = vida + 20

print("\n===== PONTOS DE VIDA =====")
print("Pontos de vida restantes:", vida)

#exercício 7

salario = 2800
bonus = 450
salario_total = salario + bonus

print("\n===== SALÁRIO =====")
print("Salário total:", salario_total)

#exercício 8

largura = 5
altura = 10
area = largura * altura

print("\n===== ÁREA =====")
print("Área:", area)

#exercício 9

titulo = "Python"
versao = 3
nota = 9.5
finalizado = False

print("\n===== INFORMAÇÕES =====")

print((type(titulo)))#str é string, ou seja, texto
print((type(versao)))#int é inteiro, ou seja, número inteiro
print((type(nota)))#float é ponto flutuante, ou seja, número com vírgula
print((type(finalizado)))#bool é booleano, ou seja, valor lógico

#exercício 10

nome = "Christian"
classe = "Bardo"
nivel = 5
vida = 100
ataque = 20
defesa = 15
possui_magia = True

poder = ataque + defesa

print("\n===============\n  PERSONAGEM  \n===============\n")
print("Nome:", nome)
print("Classe:", classe)
print("Nível:", nivel)
print("Vida:", vida)
print("Ataque:", ataque)
print("Defesa:", defesa)
print("Poder total:", poder)
print("Possui Magia:", possui_magia)

print("\n==============================")

#DESAFIO EXTRA!

nome = "Christian"
vida = 100
ouro = 50
nivel = 1

ganha_ouro = 20
recebe_dano = 30
gasta_ouro = 10
recupera_vida = 15
sobe_nivel = 1

pontos_de_vida = vida - recebe_dano + recupera_vida
quantidade_de_ouro = ouro + ganha_ouro - gasta_ouro
nivel_atual = nivel + sobe_nivel

print("\n===== STATUS DO PERSONAGEM =====")
print("Nome:", nome)
print("Pontos de vida:", pontos_de_vida)
print("Quantidade de ouro:", quantidade_de_ouro)
print("Nível atual:", nivel_atual)

