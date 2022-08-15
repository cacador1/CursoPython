from calendar import isleap
ano = int(input('Digite um ano para descobrir se ele é bissexto:'))
if isleap(ano):
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
