print('='*25)
print('Consultor de preço')
print('='*25)
preco = float(input('Qual o preço das compras? R$'))
print('1-À vista no Dinheiro/cheque')
print('2-À vista no cartão')
print('3-Em até 2x no cartão')
print('4-3x ou mais no cartão')
forma = int(input('Qual a forma de pagamento?'))
c1 = preco * 10 / 100
pav = preco - c1
c2 = preco * 5 / 100
avc = preco - c2
c3 = preco * 20 / 100
if forma == 1:
    print(f'O valor das compras é:R${pav}')
elif forma == 2:
    print(f'O valor das compras é:R${avc}')
elif forma == 3:
    print(f'O valor da parcela será R${avc/2} em 2X,o valor final será de R${avc}')
elif forma == 4:
    parc = int(input('Quantas parcelas?'))
    pc = (preco+c3)/parc
    final = preco+c3
    print(f'Sua compra será parcelada em {parc}X de R${pc:.2f} COM JUROS\nSua compra de R${preco} vai custar R${final} no final')
else:
    print('\033[31mOpção inválida,escolha umas das opções acima\033[m')

