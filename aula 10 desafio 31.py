d = float(input('Qual a distância da sua viagem?:Km'))
if d<=200:
    print(f'O valor da sua viagem é:R${d*0.50:.2f}')
else:
    print(f'O valor da sua viagem é:R${d*0.45:.2f}')
