v = float(input('Qual velocidade seu carro está? km/h:'))
cm = v-80
vm = cm*7
if v <=80:
    print('Você está dentro do limite de velocidade,não terá de pagar multa')
else:
    print('Você ultrapassou o limite de velocidade:80km/h')
    print(f'O valor da sua multa é:R${vm:.2f}')
