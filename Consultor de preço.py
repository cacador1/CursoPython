print('='*25)
print('Consultor de preço')
print('='*25)
preco = float(input('Qual o preço do produto?R$'))
print('1-Dinheiro/cheque')
print('2-À vista no cartão')
print('3-Em até 2x no cartão')
print('4-3x ou mais no cartão')
forma = int(input('Qual a forma de pagamento?'))
c1 = preco * 10 / 100
pav = preco - c1
c2 = preco * 5 / 100
avc = preco - c2
c3 = preco * 20 / 100
pc = preco + c3
if forma == 1:
    print(f'O valor do produto é:R${pav}')
elif forma == 2:
    print(f'O valor do produto é:R${avc}')
elif forma == 3:
    print(f'O valor do produto é:R${preco}')
elif forma == 4:
    print(f'O valor do produto é:R${pc}')
