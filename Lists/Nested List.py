list1 = ['uva','morango','abacaxi']
list2 = ['maracuja','laranja','abacate']

listas = [list1,list2]

#Aqui serão criados dois laços de repetição aninhados para percorrer pela lista
#Printando na tela cada item

for n in range(2):
    for c in range(3):
        print(listas[n][c].title())

print("#############################")
#Adicionando itens nas listas

list1.append('pêra')
list2.append('maçã')

#Testando declarando novamente a matriz

listas = [list1,list2]

for n in range(2):
    for c in range(4):
        print(listas[n][c].title())
