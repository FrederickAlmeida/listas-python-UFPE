n_tiktokers = int(input())
nomes = []
seguidores = []
lista_ordenada = []

for tiktoker in range(n_tiktokers):
    seguidor = input()
    nomes.append(seguidor.split("-")[0])
    seguidores.append(int(seguidor.split("-")[1]))

while len(seguidores) > 0:
    menos_seguidores = seguidores[0]
    for i in seguidores:
        if i < menos_seguidores:
            menos_seguidores = i
        elif i == menos_seguidores:
            if len(nomes[seguidores.index(menos_seguidores)]) > len(nomes[seguidores.index(i)]):
                menos_seguidores = i
            elif len(nomes[seguidores.index(menos_seguidores)]) == len(nomes[seguidores.index(i)]):
                if seguidores.index(menos_seguidores) > seguidores.index(i):
                    menos_seguidores = i
    lista_ordenada.append(f"{nomes[seguidores.index(menos_seguidores)]}-{menos_seguidores}")
    nomes.remove(nomes[seguidores.index(menos_seguidores)])
    seguidores.remove(menos_seguidores)

for seguidor in lista_ordenada:
    print(seguidor)