d = int(input('Quantos dias o carro foi alugado?:'))
km = float(input('Quantos Km foi rodado?:'))
dr = d*60
kmr = km*0.15
print(f'O valor total a ser pago é de:R${dr+kmr:.2f}')
