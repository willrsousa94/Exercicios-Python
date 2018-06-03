import random

numpc = random.randint(0,5)

numuser = input('Digite um número entre 0 e 5: ')

while(int(numuser) < 0 | int(numuser) > 5):
    print('Número incorreto')
    numuser = input('Por favor, Digite um número entre 0 e 5')

if(int(numuser) == numpc):
    print('Parabéns, você acertou!')
else:
    print('Você errou, tente novamente')

print('O número pensado pelo sistema foi: {}'.format(numpc))