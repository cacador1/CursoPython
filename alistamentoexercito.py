from datetime import date
print('='*20)
print('\033[34mSistema de consulta\033[m')
print('='*20)
print('\033[32mSiga as instruções abaixo para descobrir sua situação quanto ao alistamento do exército\033[m')
print('='*87)
sex = int(input('Qual o seu gênero?\n1-Masculino\n2-Feminino\n:'))
if sex == 1:
    ano = int(input('\033[34mQual seu ano de nascimento?\033[m'))
    atual = date.today().year
    idade = atual-ano
    if idade < 18:
        print(f'''\033[34mVocê não precisa se alistar esse ano,ainda faltam {18-idade} anos.
você deverá se alistar em {atual+18-idade}\033[m''')
    elif idade == 18:
        print('\033[32mJá está na hora de você se alistar,procure o batalhão mais proximo de sua cidade\033[m')
    elif idade > 18:
        print(f'''\033[31mVocê passou {idade-18} anos do prazo de alistamento.
você deveria ter se alistado em {atual-idade+18}\033[m''')
elif sex == 2:
    print('O alistamento militar não é obrigatório para mulheres.')
else:
    print('Opção inválida, escolha uma das opções acima!.')
