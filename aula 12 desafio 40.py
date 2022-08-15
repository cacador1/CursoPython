print('\033[35m=\033[m'*20)
print('\033[1;35mBoletim virtual\033[m')
print('\033[35m=\033[m'*20)
nota = float(input('Digite aqui a sua nota:'))
nota1 = float(input('Digite aqui a sua nota:'))
c = (nota+nota1)/2
if c < 5:
    print('Sua média foi abaixo de 5.0, você está \033[31mreprovado\033[m')
elif c <= 6.9 and c >= 5.0:
    print(f'Sua média foi {c}, você está de \033[34mrecuperação\033[m')
elif c >= 7:
    print(f'Sua média foi {c}, você está \033[34maprovado\033[m')
