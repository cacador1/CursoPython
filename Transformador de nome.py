n = str(input('Digite seu nome:')).strip()
d = n.split()
n2 = "".join(d)
print(f'Seu nome maiúsculo:{n.upper()}')
print(f'Seu nome minúsculo:{n.lower()}')
print(f'Seu nome tem {len(n2)} letras')
print(f'Seu primeiro nome é {d[0]} tem {len(d[0])} letras')





