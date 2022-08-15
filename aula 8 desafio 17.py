import math
co = float(input('Digite aqui o comprimento do cateto oposto:'))
ca = float(input('Digite aqui o comprimento do cateto adjacente:'))
hi = math.hypot(ca, co)
print(f'o comprimento da hipotenusa é:{hi:.2f}')
