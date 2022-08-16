from random import randint
from time import sleep
linha = '\033[32m=\033[m' * 40
titulo = '\033[32mJOKENPÔ\033[m'
print('\033[34mVamos jogar JOKENPÔ?\033[m')
r1 = int(input('''\033[32m[ 1 ] Sim\033[m
\033[31m[ 2 ] Não\033[m
:'''))
if r1 == 1:
    print(titulo.center(50, '='))
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('''[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
    jogador = int(input('Qual é a sua jogada?'))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print('='*25)
    print(f'O computador jogou {itens[computador]}')
    print(f'O jogador jogou {itens[jogador]}')
    print('='*25)
    if computador == 0:
        if jogador == 0:
            print('\033[33mEMPATE!\033[m')

        elif jogador == 1:
            print('\033[32mO jogador venceu!\033[m')

        elif jogador == 2:
            print('\033[32mO computador venceu!\033[m')

    elif computador == 1:
        if jogador == 0:
          print('\033[32mO compuatdor venceu!\033[m')

        elif jogador == 1:
          print('\033[33mEMPATE!\033[m')

        elif jogador == 2:
          print('\033[32mO jogador venceu!\033[m')

    elif computador == 2:
        if jogador == 0:
          print('\033[32mO jogador venceu!\033[m')

        elif jogador == 1:
          print('\033[32mO computador venceu!\033[m')

        elif jogador == 2:
          print('\033[32mEMPATE!\033[m')

elif r1 == 2:
 print('Ok, tchau!...')
else:
    print('\033[31mOpção inválida, ecsolha uma das opções acima!\033[m')
