def posicaoinput(x, y):
    auxiliar = []
    auxiliar.append(int(x))
    auxiliar.append(int(y))
    return auxiliar

def movimentojason():   # caso o x seja diferente do x do cara, tem que avançar pelo eixo do x, caso contrario, pelo eixo do y
    matriz[jason_posicao[0]][jason_posicao[1]] = "-"
    if jason_posicao[1] != sua_posicao[1]:
        if sua_posicao[1] < jason_posicao[1]:
            jason_posicao[1] -= 1
        elif sua_posicao[1] > jason_posicao[1]:
            jason_posicao[1] += 1

    elif (jason_posicao[1] == sua_posicao[1]) and (jason_posicao[0] != sua_posicao[0]):
        if sua_posicao[0] < jason_posicao[0]:
            jason_posicao[0] -= 1
        elif sua_posicao[0] > jason_posicao[0]:
            jason_posicao[0] += 1
    
    if (jason_posicao[1] == sua_posicao[1]) and (jason_posicao[0] == sua_posicao[0]):
        matriz[jason_posicao[0]][jason_posicao[1]] = "J"
        return True, matriz, jason_posicao     # fim de jogo

    matriz[jason_posicao[0]][jason_posicao[1]] = "J"
    return False, matriz, jason_posicao

def seumovimento():
    global mensagem
    if game_over == False:
        matriz[sua_posicao[0]][sua_posicao[1]] = "-"
        if procurar_gasolina:
            if gasolina_posicao[1] != sua_posicao[1]:
                if sua_posicao[1] < gasolina_posicao[1]:
                    sua_posicao[1] += 1
                elif sua_posicao[1] > gasolina_posicao[1]:
                    sua_posicao[1] -= 1

            elif (gasolina_posicao[1] == sua_posicao[1]) and (gasolina_posicao[0] != sua_posicao[0]):
                if sua_posicao[0] < gasolina_posicao[0]:
                    sua_posicao[0] += 1
                elif sua_posicao[0] > gasolina_posicao[0]:
                    sua_posicao[0] -= 1

            if (gasolina_posicao[1] == sua_posicao[1]) and (gasolina_posicao[0] == sua_posicao[0]):
                matriz[sua_posicao[0]][sua_posicao[1]] = "V"
                mensagem = "Deu bom! Peguei a Gasolina nessa rodada."
                return False, matriz, sua_posicao, mensagem

            else:
                matriz[sua_posicao[0]][sua_posicao[1]] = "V"
                mensagem = "Nao peguei nenhum objeto nessa rodada :("
                return True, matriz, sua_posicao, mensagem

        else:
            if mensagem == "Deu bom! Peguei a Gasolina nessa rodada.":
                matriz[sua_posicao[0]][sua_posicao[1]] = "V"
                mensagem = "Nao peguei nenhum objeto nessa rodada :("
                return False, matriz, sua_posicao, mensagem

            if carro_posicao[1] != sua_posicao[1]:
                if sua_posicao[1] < carro_posicao[1]:
                    sua_posicao[1] += 1
                elif sua_posicao[1] > carro_posicao[1]:
                    sua_posicao[1] -= 1

            elif (carro_posicao[1] == sua_posicao[1]) and (carro_posicao[0] != sua_posicao[0]):
                if sua_posicao[0] < carro_posicao[0]:
                    sua_posicao[0] += 1
                elif sua_posicao[0] > carro_posicao[0]:
                    sua_posicao[0] -= 1

            if (carro_posicao[1] == sua_posicao[1]) and (carro_posicao[0] == sua_posicao[0]):
                matriz[sua_posicao[0]][sua_posicao[1]] = "V"
                mensagem = "Consegui chegar no carro, agora e so ligar e fugir daqui!"
                return False, matriz, sua_posicao, mensagem

            else:
                matriz[sua_posicao[0]][sua_posicao[1]] = "V"
                mensagem = "Nao peguei nenhum objeto nessa rodada :("
                return False, matriz, sua_posicao, mensagem
    else:
        return True, matriz, sua_posicao, mensagem

def distancia_JV():
    distancia = int(((sua_posicao[0] - jason_posicao[0])**2 + (sua_posicao[1] - jason_posicao[1])**2)**0.5)
    if distancia <= 3:
        return "E melhor correr, o Jason vai me pegar!"
    elif (distancia > 3) and (distancia <= 4):
        return "Consigo ver o Jason daqui, preciso apressar o passo!"
    elif distancia > 4:
        return "Ufa, o Jason ainda esta longe, mas nao posso diminuir o ritmo."

# criando a matriz 6x6:
matriz = []
for line in range(6):
    linha = []
    for column in range (6):
        linha.append("-")
    matriz.append(linha)

# pegando as coordenadas e salvando na matriz:
sua_posicao = posicaoinput(input(), input())
matriz[sua_posicao[0]][sua_posicao[1]] = "V"
jason_posicao = posicaoinput(input(), input())
matriz[jason_posicao[0]][jason_posicao[1]] = "J"
gasolina_posicao = posicaoinput(input(), input())
matriz[gasolina_posicao[0]][gasolina_posicao[1]] = "G"
carro_posicao = posicaoinput(input(), input())
matriz[carro_posicao[0]][carro_posicao[1]] = "C"

game_over, procurar_gasolina, mensagem = False, True, ""
while not(game_over):
    game_over, matriz, jason_posicao = movimentojason()
    procurar_gasolina, matriz, sua_posicao, mensagem = seumovimento()

    for line in matriz:
        counter = 0
        for column in line:
            if counter != (len(line) - 1):
                print(column, end=" ")
            else:
                print(column, end="\n")
            counter += 1
    
    if game_over == True:
        print("Oh nao, o Jason me pegou, F total!")
    else:
        print(mensagem)
        if mensagem == "Consegui chegar no carro, agora e so ligar e fugir daqui!":
            game_over = True
        else:
            print(distancia_JV())
            print("")