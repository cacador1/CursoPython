print('\033[34m=\033[m'*35)
print('\033[1;34mAnalisador de números\033[m')
print('\033[34m=\033[m'*35)
n1 = int(input('\033[34mDigite um número:\033[m'))
n2 = int(input('\033[34mDigite outro número:\033[m'))
if n1 > n2:
    print('\033[33mO primeiro valor digitado é maior\033[m')
elif n1 < n2:
    print('\033[33mO segundo valor digitado é maior\033[m')
else:
    print('\033[31mOs dois números digitados são iguais\033[m')
