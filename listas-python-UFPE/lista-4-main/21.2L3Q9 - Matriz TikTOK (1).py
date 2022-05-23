aux = input()
N = int(aux.split()[0])
M = int(aux.split()[1])
matriz = []


# fazer uma matriz com sublistas
# L = linha e C = coluna
for L in range(N):
    aux = []
    linha = input()
    for C in range(M):
        aux.append(linha[C])
    
    matriz.append(aux)

# varrer a linha à procura de '*'
lista_index = []
for L in range(N):
    aux = []
    for C in range(M):
        if matriz[L][C] == "*":
            aux.append(C)
    
    lista_index.append(aux)

# fazer a checagem das cruzes
dot_cima = dot_baixo = dot_left = dot_right = 0
for L in range(N):  
    for C in lista_index[L]:
        aster_cima = aster_baixo = aster_left = aster_right = 0
        dot_cima = dot_baixo = dot_left = dot_right = 0
       
       # Eu recebo o valor das linhas nas variáveis cima e baixo e o valor das colunas nas variáveis right e left
        cima = L
        baixo = L
        right = C
        left = C
        while dot_cima == dot_baixo == dot_left == dot_right == 0:

            # O programa anda nos 4 sentidos e verifica o index
            cima += - 1
            if cima >= 0:
                if matriz[cima][C] == "*":
                    aster_cima += 1
                else:
                    dot_cima += 1
            else:
                dot_cima += 1

            baixo += 1
            if baixo < N:
                if matriz[baixo][C] == "*":
                    aster_baixo += 1
                else:
                    dot_baixo += 1
            else:
                dot_baixo += 1

            right += 1
            if right < M:
                if matriz[L][right] == "*":
                    aster_right += 1
                else:
                    dot_right += 1
            else:
                dot_right += 1

            left -= 1
            if left >= 0:
                if matriz[L][left] == "*":
                    aster_left += 1
                else:
                    dot_left += 1
            else:
                dot_left += 1
    # dou o break nos dois for
        if dot_right == dot_left == dot_baixo == dot_cima == 1:
            break
    if dot_right == dot_left == dot_baixo == dot_cima == 1:
        break
    
if aster_baixo == aster_cima == aster_left == aster_right > 0:
    if aster_baixo == 1:
        print("Nao foi um dos melhores, mas ta valendo...")
    elif aster_baixo == 2:
        print("Esta perfeito, quase peguei toda a premiaçao, UHUL!!")
    elif aster_baixo == 3:
        print("AEEEEW, ACHEI O PRECIOSO!!!!")
else:
    print("Puts, dessa vez nao tive sorte...")
