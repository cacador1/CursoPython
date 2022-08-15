s = float(input('Digite aqui o valor do seu sálario atual, para descobrir seu novo sálario com aumento:R$'))
s1 = s * 0.10
vs = s + s1
s2 = s * 0.15
vs2 = s + s2

if s >= 1250:
    print(f'O seu sálario com 10% de aumento é:R${vs:.2f}')
else:
    print(f'O seu sálario com 15% de aumento é:R${vs2:.2f}')
