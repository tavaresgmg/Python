# Esse programa solicita dois números inteiros e imprime: a. o produto entre o dobro do primeiro com a metade do segundo
# b. a soma do triplo do primeiro com o terceiro
# c. o terceiro elevado ao cubo

n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))
n3 = float(input('Insira o terceiro número: '))

a = (2*n1) * (n2/2)
b = (3*n1) + n3
c = n3**3

print(f"O produto do dobro do primeiro com metade do segundo: {a}\n"
      f"A soma do triplo do primeiro com o terceiro: {b}\n"
      f"O terceiro elevado ao cubo: {c}")
