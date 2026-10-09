numero_de_alunos = 25
valor_do_onibus = 600.00
valor_do_ingresso = 15.00
valor_do_lanche = 10.00

custo_dos_ingressos = numero_de_alunos * valor_do_ingresso
custo_dos_lanches = numero_de_alunos * valor_do_lanche
custo_total = custo_dos_ingressos + custo_dos_lanches + valor_do_onibus
deve_pagar = custo_total / numero_de_alunos

print("=====DEPESAS DO PASSEIO=====")
print("Custo de todos os ingressos:", custo_dos_ingressos)
print("Custo de todos os lanches:", custo_dos_lanches)
print("Custo total do passeio:", custo_total)
print("Valor que cada aluno deve pagar:", deve_pagar)
print("=============================")