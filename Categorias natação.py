print('\033[34m-=-\033[m'*11)
print('\033[1;34mConfederação Nacional de Natação\033[m')
print('\033[34m-=-\033[m'*11)
ano = int(input('Insira aqui seu ano de nascimento:'))
idade = 2022-ano
if idade <= 9:
    print('Sua categoria é:\033[1;34mMirim\033[m')
elif idade <= 14:
    print('Sua categoria é:\033[1;34mInfantil\033[m')
elif idade <= 19:
    print('Sua categoria é:\033[1;34mJunior\033[m')
elif idade <= 20:
    print('Sua categoria é:\033[1;34mSênior\033[m')
elif idade > 20:
    print('Sua categoria é:\033[1;34mMaster\033[m')
