print('='*25)
print('Calculadora IMC')
print('='*25)
peso = float(input('Digite aqui o seu peso:'))
altura = float(input('Digite aqui a sua altura:'))
c1 = altura**2
imc = peso/c1
if imc < 18.5:
    print('Você está \033[1;31mabaixo\033[m do peso')

elif imc > 18.5 and imc < 24:
    print('Você está no peso \033[1;32mideal\033[m')

elif imc > 25 and imc < 29:
    print('Você está com \033[1;31msobrepeso\033[m')

elif imc > 30 and imc < 39:
    print('Você está com \033[1;31mobesidade\033[m')

elif imc > 40:
    print('Você está com \033[1;31mobesidade mórbida\033[m')
