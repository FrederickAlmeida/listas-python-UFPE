def direcao(linha_link, coluna_link):
    if linha_link < (dimensao_labirinto - 1) and (labirinto[linha_link + 1][coluna_link] == "." or labirinto[linha_link + 1][coluna_link] == "Z"):   # sul
        mensagem = "Caminharei pelo Sul e certamente irei encontrar-te, Zelda"
        posicao_link[0] += 1
        return posicao_link, mensagem

    elif coluna_link < (dimensao_labirinto - 1) and (labirinto[linha_link][coluna_link + 1] == "." or labirinto[linha_link][coluna_link + 1] == "Z"): # leste
        mensagem = "Caminharei pelo Leste e certamente irei encontrar-te, Zelda"
        posicao_link[1] += 1
        return posicao_link, mensagem

    elif linha_link > 0 and (labirinto[linha_link - 1][coluna_link] == "." or labirinto[linha_link - 1][coluna_link] == "Z"): # norte
        mensagem = "Caminharei pelo Norte e certamente irei encontrar-te, Zelda"
        posicao_link[0] -= 1
        return posicao_link, mensagem

    elif coluna_link > 0 and (labirinto[linha_link][coluna_link - 1] == "." or labirinto[linha_link][coluna_link - 1] == "Z"): # oeste
        mensagem = "Caminharei pelo Oeste e certamente irei encontrar-te, Zelda"
        posicao_link[1] -= 1
        return posicao_link, mensagem

    else:
        return ["", ""], "HAHAHAHA você nunca irá resgatá-la, Link!!!"

def atualizarlabirinto(linha_link, coluna_link, printar):
    if labirinto[linha_link][coluna_link] != "Z":
        labirinto[linha_link][coluna_link] = "L"
        return labirinto, printar

    elif labirinto[linha_link][coluna_link] == "Z":
        labirinto[linha_link][coluna_link] = "L"
        printarlabirinto(labirinto)
        print(f"{printar}\n")
        printar = "Vamos embora daqui Princesa!!!"
        return labirinto, printar

def printarlabirinto(labirinto):
    for linha in labirinto:
        i = 0
        for coluna in linha:
            if i < (len(linha) - 1):
                print(coluna, end="")
            elif i == (len(linha) - 1):
                print(coluna)
            i += 1

def movimetolink(linha, coluna):
    # determinação a direção que o link seguirá
    posicao_link, printar = direcao(linha, coluna)
    # atualizar a posicao do link no labirinto
    if posicao_link == ["", ""]:
        return printar
    else:
        labirinto, printar = atualizarlabirinto(posicao_link[0], posicao_link[1], printar)
        printarlabirinto(labirinto)
        if printar == "Vamos embora daqui Princesa!!!":
            return printar
        else:
            print(f"{printar}\n")
    
    return movimetolink(posicao_link[0], posicao_link[1])


dimensao_labirinto = int(input())
posicao_link = [int(input()), int(input())] #linha, coluna
labirinto = []

# criando o labirinto
for linha in range(dimensao_labirinto):
    lista_aux = []
    entrada = input()
    for char in entrada:
        lista_aux.append(char)
    labirinto.append(lista_aux)

print(movimetolink(posicao_link[0], posicao_link[1]))