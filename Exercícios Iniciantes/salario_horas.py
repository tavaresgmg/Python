# Esse programa calcula seu salario mensal se infromada quantas horas trabalhadas e o valor recebido por hora

horas = float(input("Quantas horas voce trabalhou esse mes ? "))
valor_hora = float(input("Quanto voce recebe por hora ? "))

salario = horas*valor_hora

print(f"Seu salario esse mes sera de R${salario}")