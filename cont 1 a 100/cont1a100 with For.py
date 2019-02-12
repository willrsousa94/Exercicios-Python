n = 1
s1 = "Critical"
s2 = "Damage"
for n in range(100):
    if(n%5==0 and n%3==0):
        print(s1 + " " + s2)
    elif(n%5==0):
        print(s2)
    elif(n%3==0):
        print(s1)
    else:
        print(n)
        
"""
Diferente de outras linguagens que conheci, no Python o for funciona
de uma forma diferente (porém a ideia é a mesma e, até mais simples)
Em vez de fazer um simples for(n==0;n<=100;n++)
Se faz for n in range(100)
A ideia é a mesma, mesmo que escrita de forma diferente
Quando coloca um in range(100), simplesmente explica ao Python que deseja
que a função aumente a variável n até chegar em 100, mais prático!
"""
