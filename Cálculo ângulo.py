import math

an = float(input('Digite o ângulo que deseja:'))
r = math.radians(an)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)
print(f'Se o ângulo for {an}\nO seno será:{s:.2f}\nO cosseno será:{c:.2f}\nE a tangente será:{t:.2f}')
