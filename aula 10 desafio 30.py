n = int(input('Digite um número para descobrir se ele é par ou ímpar:'))
resto = n % 2
if resto == 0:
    print(f'O número {n} é par')
else:
    print(f'O número {n} é ímpar')


