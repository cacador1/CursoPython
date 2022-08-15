import random
n1 = str(input('Digite aqui o nome do primero aluno:'))
n2 = str(input('Digite o nome do segundo aluno:'))
n3 = str(input('Digite o nome do terceiro aluno:'))
n4 = str(input('Digite o nome do quarto aluno:'))
l = [n1,n2,n3,n4]
s = random.choice(l)
print(f'O aluno sorteado para apagar o quadro foi:{s}')

