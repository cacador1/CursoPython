print('\033[34m=\033[m' * 40)
print('\033[34mConsulta de financiamento bancário\033[m')
print('\033[34m=\033[m' * 40)
valorcasa = float(input('Qual o valor do imóvel?R$'))
salario = float(input('Qual o valor do seu salário?R$'))
tempo = int(input('Em quantos anos você deseja pagar?'))
tempo1 = tempo * 12
valorp = valorcasa / tempo1
c1 = salario * 30/100
if valorp <= c1:
    print(f'Você poderá comprar este imóvel,o valor da prestação será {valorp:.2f} por mês por {tempo} anos')
else:
    print(f'Você não pode comprar este imóvel,o valor da prestação é {valorp:.2f},o valor excede 30% do seu sálario')
