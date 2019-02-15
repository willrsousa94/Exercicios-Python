question = int(input('Quer saber o cubo de 1 até qual número? '))
cubes = [value**3 for value in range(1,question)]

for cube in cubes:
    print(str(round(cube **(1/3))) + " ao cubo = " + str(cube))
