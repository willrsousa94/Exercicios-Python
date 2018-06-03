print('Exercício 23 - Curso em Vídeo')

numero = (input('Digite um número de 0 a 9999: '))

while(int(numero) < 0 or int(numero) > 9999):
    print('ERRO! Número não está entre 0 e 9999!')
    numero = input('Digite novamente: ')

    if len(numero) == 1:
        numero = '000' + numero
    elif len(numero) == 2:
        numero = '00' + numero
    elif len(numero) == 3:
        numero = '0'+ numero


    print('Unidade: {}'.format(numero[3]))
    print('Dezena: {}'.format(numero[2]))
    print('Centena: {}'.format(numero[1]))
    print('Milhar: {}'.format(numero[0]))