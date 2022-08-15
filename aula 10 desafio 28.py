from random import randint
from time import sleep
print('_' *40)
print ('Estou pensando em um número de 0 á 5...')
print('_' *40)
n = int(input('Tente advinhar o número que estou pensando\n:'))
print('Processando...')
sleep(2)
s = randint(0, 5)
if n==s:
    print(f'Parabéns,o número que eu pensei foi:{s}!')
else:
    print(f'O número que eu pensei foi {s}, e não {n}!')
