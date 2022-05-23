def organizar_armadilhas(qtd_casas):
    armadilhas = {}
    if qtd_casas >=2 and qtd_casas <= 10:
        for armadilha in range(qtd_casas):  # salvar a posição das armadilhas; 1 = esquerda, 2 = direita
            armadilhas[armadilha] = int(input())
        return armadilhas, False

    else:
        return f"Faixa não permitida", True

def organizar_jogadores():
    lista_jogadores = []
    for jogador in range(3):    # salvar o nome dos jogadores e seus apelidos
        lista_jogadores.append((input(), input()))

    return lista_jogadores

def atualizar_armadilhas(armadilhas):
    if len(armadilhas) > 0:
        for i in range(len(armadilhas)):
            armadilhas[i] = armadilhas[i + 1]   # atualizar o index
        armadilhas.pop(len(armadilhas)-1)

    return armadilhas

def lista_atualizada(jogadores, jogadores_mortos):
    for jogador in jogadores_mortos:
        jogadores.remove(jogador)
    return jogadores

def o_jogo(armadilhas, lista_jogadores, ganhador):
    remover_armadilha = False
    jogadores_mortos = []
    for jogadores in lista_jogadores:
        if len(armadilhas.items()) > 0: # caso ainda tenha obstaculos:
            escolha = int(input())
                
            if escolha == armadilhas[0]: # caso o jogador escolha o casa com armadilha
                if len(lista_jogadores) == 1:   # caso esse seja o ultimo jogador:
                    print("Todos os jogadores morreram!")
                    lista_jogadores.remove(jogadores)

                    return lista_jogadores, armadilhas, False, ganhador

                else:   # caso não seja o ultimo jogador
                    if len(jogadores_mortos) == 2:
                        print("Todos os jogadores morreram!")
                    
                        return lista_jogadores, armadilhas, False, ganhador

                    else:
                        print(f"{jogadores[0]} caiu de uma altura de 30 metros e morreu! :O")
                        jogadores_mortos.append(jogadores)  # adicionar esse jogador à lista de jogadores mortos, para depois remover da lista de jogadores

            elif escolha != armadilhas[0]: # caso o jogador escolha a casa sem armadilha:
                if len(armadilhas) > 1:
                    remover_armadilha = True
                    print(f"{jogadores[0]} pulou uma casa!")

                else:   # caso esteja na ultima casa, não devemos printar a msg
                    ganhador = jogadores
                    remover_armadilha = True
                    print(f"{jogadores[0]}, mais conhecido como {jogadores[1]}, ganhou o jogo! Parabéns!")

                    return lista_jogadores, armadilhas, False, ganhador
    
    # atualizar as armadilhas
    if remover_armadilha:
        armadilhas.pop(0)
        armadilhas = atualizar_armadilhas(armadilhas)
                
    lista_jogadores = lista_atualizada(lista_jogadores, jogadores_mortos)
    
    if len(lista_jogadores) > 0:
        return lista_jogadores, armadilhas, True, ganhador
    else:
        return lista_jogadores, armadilhas, False, ganhador

total_casas = int(input())
posicao_armadilhas, jogadores = {}, []
ganhador_do_jogo = ""

posicao_armadilhas, encerrar_programa = organizar_armadilhas(total_casas)

if encerrar_programa:
    print(posicao_armadilhas)
    continuar_jogo = False

else:
    jogadores = organizar_jogadores()
    continuar_jogo = True

while continuar_jogo:       # o jogo (perdi)
    jogadores, posicao_armadilhas, continuar_jogo, ganhador_do_jogo = o_jogo(posicao_armadilhas, jogadores, ganhador_do_jogo)
