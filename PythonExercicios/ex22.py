print('Exercício 22 - Curso em Vídeo')

nome = input('Digite seu nome completo: ')

print('Com letras maiúsculas: {}'.format(nome.upper()))
print('Com letras minúsculas: {}'.format(nome.lower()))
print('Número de letras: {}'.format(len(nome.replace(' ','').strip())))
print('Tamanho do primeiro nome: {}'.format(len(nome.split()[0])))