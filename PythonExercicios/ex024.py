print('Exercício 24 - Curso em Vídeo')

cidade = input('Digite o nome de uma cidade: ')

if(cidade.upper().split()[0] == "SANTO"):
    print('A cidade {} começa com SANTO'.format(cidade))
else:
    print('A cidade {} não começa com SANTO'.format(cidade))