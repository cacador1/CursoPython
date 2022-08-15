import random
print('___Sorteando lista de alunos___')
print('Digite o nome de 4 alunos.')
a1 = input('1°Aluno:')
a2 = input('2°Aluno:')
a3 = input('3°Aluno:')
a4 = input('4°Aluno:')
l = [a1, a2,a3,a4]
random.shuffle(l)
print(f'A lista sorteada foi:{l}')
