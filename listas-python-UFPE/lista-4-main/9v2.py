dimensoes = input().split(" ")
matriz = []
infos_matriz = []


for line in range(int(dimensoes[0])):
    lista_aux = []
    aux = input()
    for column in range(int(dimensoes[1])):
        lista_aux.append(aux[column])
    matriz.append(lista_aux)

# descobrir o centro da cruz analisando a quantidade de asteriscos em cada linha
asteriscos = []
aux = 0
for line in matriz:
    asteriscos.append(0)
    for column in line:
        if column == "*":
            asteriscos[aux] += 1
    aux += 1

# infos_matriz[0]: a linha que tiver mais asteriscos será a linha central da cruz
infos_matriz.append(asteriscos.index(max(asteriscos)))
# infos_matriz[1]: o index do elementro central da cruz
infos_matriz.append(matriz[infos_matriz[0]].index("*") + max(asteriscos)//2)

asteriscos_esquerda = 0
asteriscos_direita = 0
asteriscos_cima = 0
asteriscos_baixo = 0

# checar esquerda
for element in range(0, infos_matriz[1]):
    if matriz[infos_matriz[0]][element] == "*":
        asteriscos_esquerda += 1
# checar direita
for element in range(infos_matriz[1]+1, dimensoes[0]+1):
    if matriz[infos_matriz[0]][element]:
        asteriscos_direita += 1
# chechar cima
for linha in range(0, infos_matriz[0]):
    for coluna in range(dimensoes[1]):
        if matriz[linha][coluna] == "*":
            asteriscos_cima += 1
# checar baixo
for linha in range(infos_matriz[0]+1, dimensoes[0]+1):
    for coluna in range(dimensoes[1]):
        if matriz[linha][coluna] == "*":
            asteriscos_baixo += 1


print(*matriz, sep="\n")
print(*asteriscos, sep="\n")
print(*infos_matriz, sep="\n")