dimensoes = input().split(" ")
matriz = []
infos_matriz = []

for i in range(int(dimensoes[0])):  # salvar a matriz
    matriz.append(input())

for line in matriz:     # descobrir o centro e o tamanho da matriz
    if line.count("*") > 1:
        infos_matriz.append(matriz.index(line))                 # salvar o index da linha do centro dessa matriz
        infos_matriz.append(line.index("*"))                    # salvar o index do primeiro asterisco do centro
        infos_matriz.append(int(((line.count("*")) - 1)/2))     # salvar o tamanho da matriz

if len(infos_matriz) >= 3:
    if infos_matriz[2] == 1:    # caso a matriz tenha tamanho igual a 1:
        if (matriz[infos_matriz[0]][infos_matriz[1]:infos_matriz[1]+3] == "***"): # a linha do centro deve ter apenas 3 asteriscos e todos devem estar juntos
            if int(dimensoes[0]) > 3:
                if (matriz[infos_matriz[0]][infos_matriz[1]-1] != "*") and (matriz[infos_matriz[0]][infos_matriz[1]+infos_matriz[2]+1] != "*"):
                    condicao_horizontal = True
                else:
                    condicao_horizontal = False
            elif dimensoes[0] == "3":
                condicao_horizontal = True
        else:
            condicao_horizontal = False
        if (matriz[infos_matriz[0]-1][infos_matriz[1]+infos_matriz[2]] == "*"):     # a parte superior, deve ter 1 asterisco e nenhum asterisco a cima dele
            if ((infos_matriz[0]-2 >= 0) and (matriz[infos_matriz[0]-2][infos_matriz[1]+infos_matriz[2]] != "*")) or (infos_matriz[0]-2 < 0):
                condicao_superior = True
            else:
                condicao_superior = False
        else:
            condicao_superior = False
        if (matriz[infos_matriz[0]+1][infos_matriz[1]] == "*"):     # a parte inferior deve ter 1 asterisco e nenhum abaixo deele
            if ((infos_matriz[0]+2 > infos_matriz[2]*2+1) and (matriz[infos_matriz[0]+2][infos_matriz[1]+infos_matriz[2]] != "*")) or ((infos_matriz[0]+2) == (infos_matriz[2]*2+1)):
                condicao_inferior = True
            else:
                condicao_inferior = False
        else:
            condicao_inferior = False

    elif infos_matriz[2] == 2:
        if (matriz[infos_matriz[0]][infos_matriz[1]:infos_matriz[1]+5] == "*****"): # a linha do centro deve ter apenas 5 asteriscos, e todos devem estar juntos
            if int(dimensoes[0]) > 5:
                if (matriz[infos_matriz[0]][infos_matriz[1]-1] != "*") and (matriz[infos_matriz[0]][infos_matriz[1]+infos_matriz[2]+1] != "*"):
                    condicao_horizontal = True
                else:
                    condicao_horizontal = False
            elif dimensoes[0] == "5":
                condicao_horizontal = True
        else:
            condicao_horizontal = False
        if (matriz[infos_matriz[0]-1][infos_matriz[1]+infos_matriz[2]] == "*") and (matriz[infos_matriz[0]-2][infos_matriz[1]+infos_matriz[2]] == "*"): # a parte superior deve ter 2 asteriscos e nenhum a cima deles
            if (((infos_matriz[0]-3) >= 0) and (matriz[infos_matriz[0]-3][infos_matriz[1]+infos_matriz[2]] != "*")) or (infos_matriz[0]-3 < 0):
                condicao_superior = True
            else:
                condicao_superior = False
        else:
            condicao_superior = False
        if (matriz[infos_matriz[0]+1][infos_matriz[1]+infos_matriz[2]] == "*") and (matriz[infos_matriz[0]+2][infos_matriz[1]+infos_matriz[2]] == "*"): # a parte inferior deve ter 2 asteriscos e nenhum asterisco abaixo deles
            if ((infos_matriz[0]+3 > ((infos_matriz[2]*2)+1)) and (matriz[infos_matriz[0]+3][infos_matriz[1]+infos_matriz[2]] != "*")) or ((infos_matriz[0]+3) == (infos_matriz[2]*2+1)): 
                condicao_inferior = True
            else:
                condicao_inferior = False
        else:
            condicao_inferior = False

    elif infos_matriz[2] == 3:
        if (matriz[infos_matriz[0]][infos_matriz[1]:infos_matriz[1]+7] == "*******"): # a linha do centro deve ter apenas 7 asteriscos, e todos devem estar juntos
            if int(dimensoes[0]) > 7:
                if (matriz[infos_matriz[0]][infos_matriz[1]-1] != "*") and (matriz[infos_matriz[0]][infos_matriz[1]+infos_matriz[2]+1] != "*"):
                    condicao_horizontal = True
                else:
                    condicao_horizontal = False
            elif dimensoes[0] == "7":
                condicao_horizontal = True
        else:
            condicao_horizontal = False
        if (matriz[infos_matriz[0]-1][infos_matriz[1]+infos_matriz[2]] == "*") and (matriz[infos_matriz[0]-2][infos_matriz[1]+infos_matriz[2]] == "*") and (matriz[infos_matriz[0]-3][infos_matriz[1]+infos_matriz[2]] == "*"): # a parte supeior deve ter 3 asteriscos, e nenhum acima deles
            if ((infos_matriz[0]-4 >= 0) and (matriz[infos_matriz[0]-4][infos_matriz[1]+infos_matriz[2]] != "*")) or (infos_matriz[0]-4 < 0):
                condicao_superior = True
            else:
                condicao_superior = False
        else:
            condicao_superior = False
        if (matriz[infos_matriz[0]+1][infos_matriz[1]+infos_matriz[2]] == "*") and (matriz[infos_matriz[0]+2][infos_matriz[1]+infos_matriz[2]] == "*") and (matriz[infos_matriz[0]+3][infos_matriz[1]+infos_matriz[2]] == "*"): # a parte inferior deve ter apenas 3 asterioscos e nenhum abaixo deles
            if ((infos_matriz[0]+4 > infos_matriz[2]*2+1) and (matriz[infos_matriz[0]+4][infos_matriz[1]+infos_matriz[2]] != "*")) or ((infos_matriz[0]+4) == (infos_matriz[2]*2+1)):
                condicao_inferior = True
            else:
                condicao_inferior = False
        else:
            condicao_inferior = False
    else:
        condicao_superior, condicao_horizontal, condicao_inferior = False, False, False
else:
    condicao_superior, condicao_horizontal, condicao_inferior = False, False, False

if (condicao_horizontal == True) and (condicao_inferior == True) and (condicao_superior == True):
    if infos_matriz[2] == 1:
        print("Nao foi um dos melhores, mas ta valendo...")
    elif infos_matriz[2] == 2:
        print("Esta perfeito, quase peguei toda a premiaçao, UHUL!!")
    elif infos_matriz[2] == 3:
        print("AEEEEW, ACHEI O PRECIOSO!!!!")
else:
    print("Puts, dessa vez nao tive sorte...")