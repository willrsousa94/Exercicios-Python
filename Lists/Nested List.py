list1 = ['uva','morango','abacaxi']
list2 = ['maracuja','laranja','abacate']

listas = [list1,list2]

#Aqui serão criados dois laços de repetição aninhados para percorrer pela lista
#Printando na tela cada item

for n in range(len(listas)):
    for c in range(len(listas[n])):
        print(listas[n][c].title())

print("#############################")
#Adicionando itens nas listas

listas[0].append('pêra')
listas[1].append('maçã')

#Testando acrescentando novos itens as listas list1 e list2 diretamente pela matriz

for n in range(len(listas)):
    for c in range(len(listas[n])):
        print(listas[n][c].title())
