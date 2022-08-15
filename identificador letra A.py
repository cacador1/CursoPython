f = str(input('Digite uma frase:')).upper().strip()
print(f'A letra A aparece {f.count("A")} vezes')
print(f'A primeira ocorrência da letra A é na:{f.find("A")+1}°posição')
print(f'A última ocorrência da letra A é na:{f.rfind("A")}°posição')
