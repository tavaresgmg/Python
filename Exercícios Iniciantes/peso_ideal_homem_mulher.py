# Esse programa mostra o peso ideal conforme o gênero

altura = float(input('Insira sua altura: '))

sexo = input('Voce é do sexo masculino (M) ou feminino (F) ? ')

if sexo == 'M':
    peso = (72.7*altura) - 58

else:
    peso = (62.1*altura) - 44.7

print(f'Seu peso ideal é: {peso}')