num = int(input('Digite um núemro inteiro:'))
print('''Escolha uma das bases para conversão:
1-Converter para BINÁRIO
2-Converter para OCTAL
3-Converter para HEXADECIMAL''')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual á {num:b}')
elif opcao == 2:
    print(f'{num} covertido para OCTAL é igual á {num:o}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual á {num:x}')
else:
    print('\033[31mOpção inválida. Por favor, digite uma das opções indicadas.\033[m')
